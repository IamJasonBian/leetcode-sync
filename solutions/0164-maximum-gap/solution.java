class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length < 2) return 0;

        int hi = 0, lo = Integer.MAX_VALUE, ans = 0;
        for (int n : nums) {
            hi = Math.max(hi, n);
            lo = Math.min(lo, n);
        }

        int bsize = Math.max(1, (hi - lo) / (nums.length - 1));
        int numBuckets = (hi - lo) / bsize + 1;
        List<List<Integer>> buckets = new ArrayList<>(numBuckets);
        for (int i = 0; i < numBuckets; i++) {
            buckets.add(new ArrayList<>());
        }

        for (int n : nums) {
            int idx = (n - lo) / bsize;
            buckets.get(idx).add(n);
        }

        int currhi = 0;
        for (List<Integer> b : buckets) {
            if (b.isEmpty()) continue;
            int prevhi = currhi != 0 ? currhi : b.get(0), currlo = b.get(0);

            for (int n : b) {
                currhi = Math.max(currhi, n);
                currlo = Math.min(currlo, n);
            }

            ans = Math.max(ans, currlo - prevhi);
        }

        return ans;
    }
}
