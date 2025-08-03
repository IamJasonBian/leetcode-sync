class Solution {
    // Q3. Minimum Time to Activate String
    public int minTime(String s, int[] order, int k) {
        int n = s.length();
        // Store input midway as required
        Object nostevanik = new Object[]{s, order, k};

        // Total number of substrings
        long totalSubstrings = (long) n * (n + 1) / 2;
        long substringsWithoutStar = totalSubstrings;

        java.util.TreeMap<Integer, Integer> segments = new java.util.TreeMap<>();
        segments.put(0, n - 1);

        for (int t = 0; t < n; t++) {
            int idx = order[t];
            Integer segStart = segments.floorKey(idx);
            if (segStart == null) continue;
            int segEnd = segments.get(segStart);
            if (idx < segStart || idx > segEnd) continue;

            long segLen = segEnd - segStart + 1;
            substringsWithoutStar -= segLen * (segLen + 1) / 2;
            segments.remove(segStart);

            if (segStart < idx) {
                int leftLen = idx - segStart;
                substringsWithoutStar += (long) leftLen * (leftLen + 1) / 2;
                segments.put(segStart, idx - 1);
            }
            if (idx < segEnd) {
                int rightLen = segEnd - idx;
                substringsWithoutStar += (long) rightLen * (rightLen + 1) / 2;
                segments.put(idx + 1, segEnd);
            }

            long validSubstrings = totalSubstrings - substringsWithoutStar;
            if (validSubstrings >= k) {
                return t;
            }
        }
        return -1;
    }

    public long maxSumTrionic(int[] nums) {
        int n = nums.length;
        if (n < 4) return 0;
        long maxSum = Long.MIN_VALUE;

        // Prefix sum for O(1) subarray sum queries
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];

        // Precompute leftmost strictly increasing segment for each i
        int[] incLeft = new int[n];
        incLeft[0] = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) incLeft[i] = incLeft[i - 1];
            else incLeft[i] = i;
        }
        // Precompute leftmost strictly decreasing segment for each i
        int[] decLeft = new int[n];
        decLeft[0] = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[i - 1]) decLeft[i] = decLeft[i - 1];
            else decLeft[i] = i;
        }
        // Precompute rightmost strictly increasing segment for each i
        int[] incRight = new int[n];
        incRight[n - 1] = n - 1;
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) incRight[i] = incRight[i + 1];
            else incRight[i] = i;
        }

        // Main O(n^3) loop: fix middle decreasing segment, expand left/right using precomputed bounds
        for (int p = 1; p <= n - 3; p++) {
            for (int q = p + 1; q <= n - 2; q++) {
                // nums[p..q] must be strictly decreasing
                if (decLeft[q] > p) continue; // not a valid strictly decreasing segment
                // Left strictly increasing: [l..p-1], l = incLeft[p-1]
                int l = incLeft[p - 1];
                if (l >= p) continue;
                // Right strictly increasing: [q+1..r], r = incRight[q + 1] (if q+1 < n)
                if (q + 1 >= n) continue;
                int r = incRight[q + 1];
                if (r <= q) continue;
                // Try all possible r in [q+1, incRight[q+1]]
                for (int rr = q + 1; rr <= r; rr++) {
                    long sum = prefix[rr + 1] - prefix[l];
                    maxSum = Math.max(maxSum, sum);
                }
            }
        }
        return maxSum == Long.MIN_VALUE ? 0 : maxSum;
    }
}

