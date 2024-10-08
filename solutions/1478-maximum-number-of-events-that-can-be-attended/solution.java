class Solution {
    private int[] t;
    public int maxEvents(int[][] events) {
        int n = 100000;
        t = new int[4 * (n + 1)];
        build(1, 1, n);
        
        Arrays.sort(events, (a, b) -> (a[1] - b[1]));
        
        int cnt = 0;
        for (int[] event : events) {
            int firstAvailable = getFirstAvailable(1, 1, n, event[0], event[1]);
            if (event[0] <= firstAvailable && firstAvailable <= event[1]) {
                cnt++;
                update(1, 1, n, firstAvailable);
            }
        }
        return cnt;
    }
    
    private void build(int v, int tl, int tr) {
        if (tl == tr) {
            t[v] = tl;
        } else {
            int tm = tl + (tr - tl) / 2;
            build(2 * v, tl, tm);
            build(2 * v + 1, tm + 1, tr);
            t[v] = Math.min(t[2 * v], t[2 * v + 1]);
        }
    }
    
    private void update(int v, int tl, int tr, int pos) {
        if (tl == tr) {
            t[v] = Integer.MAX_VALUE;
        } else {
            int tm = tl + (tr - tl) / 2;
            if (pos <= tm)
                update(2 * v, tl, tm, pos);
            else
                update(2 * v + 1, tm + 1, tr, pos);
            t[v] = Math.min(t[v * 2], t[v * 2 + 1]);
        }   
    }
    
    // getFirstAvailable in between [tl, tr] given event [l, r]
    private int getFirstAvailable(int v, int tl, int tr, int l, int r) {
        if (l <= tl && tr <= r) {
            return t[v];
        } 
        int tm = tl + (tr - tl) / 2;
        if (l <= tm) {
            int left = getFirstAvailable(2 * v, tl, tm, l, r);
            if (left != Integer.MAX_VALUE) {
                return left;
            }
        }
        if (tm < r) {
            int right = getFirstAvailable(2 * v + 1, tm + 1, tr, l, r);
            if (right != Integer.MAX_VALUE) {
                return right;
            }
        }
        return Integer.MAX_VALUE;
    }
}
