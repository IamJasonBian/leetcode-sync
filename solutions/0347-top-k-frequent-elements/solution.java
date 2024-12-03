class Solution {

    class Group {
        int value;
        int occ;
        Group(int value, int occ) {
            this.value = value;
            this.occ = occ;
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        Arrays.sort(nums);

        PriorityQueue<Group> q = new PriorityQueue<>(new Comparator<Group>() {
            @Override
            public int compare(Group g1, Group g2) {
                return Integer.compare(g1.occ, g2.occ);
            }
        });

        int curr = nums[0];
        int count = 0;
        int times = 1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != curr) {

                if (times > k) {
                    if (q.peek().occ < count) {
                        q.remove();
                        q.add(new Group(curr, count));
                    }
                } else {
                    q.add(new Group(curr, count));
                }
                count = 0;
                curr = nums[i];
                i--;
                times++;
            } else
                count++;
        }

        if (times > k) {
            if (q.peek().occ < count) {
                q.remove();
                q.add(new Group(curr, count));
            }
        } else {
            q.add(new Group(curr, count));
        }

        int [] ans = new int[q.size()];
        int idx=0;
        while (!q.isEmpty()) {
            ans[idx++]=q.poll().value;
        }

        return ans;
    }
}
