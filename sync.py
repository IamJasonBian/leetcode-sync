#!/usr/bin/env python3
"""
LeetCode Sync Script
Pulls submission data from the alfa-leetcode-api and accumulates it over time.
Each run adds new submissions to data/all_submissions.json.

For FULL historical sync (all 639+ problems with source code),
use the joshcai/leetcode-sync GitHub Action with valid LeetCode session cookies.

This script handles the public API (no auth needed) as a supplement.

Usage:
    python3 sync.py
    python3 sync.py --username slenderman73
"""

import json
import os
import sys
import time
import urllib.request
from datetime import datetime

USERNAME = os.environ.get("LEETCODE_USERNAME", "slenderman73")
BASE_URL = "https://alfa-leetcode-api.onrender.com"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def fetch(path, retries=3, delay=2):
    url = f"{BASE_URL}/{path}"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", "leetcode-sync/1.0")
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                print(f"  Rate limited, waiting {delay}s...")
                time.sleep(delay)
                delay *= 2
                continue
            raise
        except Exception:
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            raise
    return None


def sync_submissions():
    os.makedirs(DATA_DIR, exist_ok=True)

    username = USERNAME
    for i, arg in enumerate(sys.argv):
        if arg == "--username" and i + 1 < len(sys.argv):
            username = sys.argv[i + 1]

    print(f"Syncing LeetCode data for: {username}")

    print("Fetching profile...")
    profile = fetch(f"{username}")
    time.sleep(1)

    print("Fetching solved stats...")
    solved = fetch(f"{username}/solved")
    time.sleep(1)

    print("Fetching skill stats...")
    skills = fetch(f"{username}/skill")
    time.sleep(1)

    print("Fetching language stats...")
    langs = fetch(f"{username}/language")
    time.sleep(1)

    print("Fetching recent AC submissions...")
    ac_subs = fetch(f"{username}/acSubmission?limit=20")
    time.sleep(1)

    print("Fetching question progress...")
    progress = fetch(f"{username}/progress")

    snapshot = {
        "username": username,
        "fetched_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "profile": profile,
        "solved": solved,
        "skills": skills,
        "languages": langs,
        "recent_accepted_submissions": ac_subs,
        "progress": progress,
    }

    with open(os.path.join(DATA_DIR, "profile_snapshot.json"), "w") as f:
        json.dump(snapshot, f, indent=2)
    print("\nSaved profile_snapshot.json")

    accum_path = os.path.join(DATA_DIR, "all_submissions.json")
    accumulated = {}
    if os.path.exists(accum_path):
        with open(accum_path) as f:
            accumulated = json.load(f)

    new_count = 0
    if ac_subs and "submission" in ac_subs:
        for s in ac_subs["submission"]:
            slug = s["titleSlug"]
            if slug not in accumulated:
                accumulated[slug] = s
                new_count += 1

    with open(accum_path, "w") as f:
        json.dump(accumulated, f, indent=2)

    print(f"New submissions this sync: {new_count}")
    print(f"Total accumulated: {len(accumulated)} unique problems")

    if solved:
        print(f"\nProfile Summary:")
        print(f"  Total solved: {solved.get('solvedProblem', '?')}")
        print(f"  Easy: {solved.get('easySolved', '?')} | Medium: {solved.get('mediumSolved', '?')} | Hard: {solved.get('hardSolved', '?')}")


if __name__ == "__main__":
    sync_submissions()
