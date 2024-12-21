class Solution {
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        int[][] pyramid = new int[6][6];
        int depth = bottom.length() - 1;
        for(int i = 0; i < bottom.length(); i++){
            pyramid[depth][i] = bottom.charAt(i) - 'A';
        }
        boolean[][][] dict = new boolean[6][6][6];
        for(String s : allowed){
            dict[s.charAt(0) - 'A'][s.charAt(1) - 'A'][s.charAt(2) - 'A'] = true;
        }
        return dfs(pyramid, dict, depth, 0);
    }
    private boolean dfs(int[][] pyramid, boolean[][][] dict, int depth, int index){
        if(depth == 0){
            return true;
        }
        if(depth == index){
            return dfs(pyramid, dict, depth - 1, 0);
        }
        int first = pyramid[depth][index];
        int second = pyramid[depth][index + 1];
        for(int i = 0; i < 6; i++){
            if(dict[first][second][i]){
                int pre = pyramid[depth - 1][index];
                pyramid[depth - 1][index] = i;
                if(dfs(pyramid, dict, depth, index + 1)){
                    return true;
                }
                pyramid[depth - 1][index] = pre;
            }
        }
        return false;
    }
}
