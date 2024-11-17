class Solution {
    boolean visited [] = new boolean[10];
    int smallestDistanceSum = Integer.MAX_VALUE;
    private int findDistance(int[] worker, int[] bike) {
        return Math.abs(worker[0] - bike[0]) + Math.abs(worker[1] - bike[1]);
    }
    
    private void minimumDistanceSum(int[][] workers, int workerIndex, int[][] bikes, int currDistanceSum) {
        if (workerIndex >= workers.length) {
            smallestDistanceSum = Math.min(smallestDistanceSum, currDistanceSum);
            return;
        }
        if (currDistanceSum >= smallestDistanceSum) {
            return;
        }
        for (int bikeIndex = 0; bikeIndex < bikes.length; bikeIndex++) {
            if (!visited[bikeIndex]) {
                visited[bikeIndex] = true;
                minimumDistanceSum(workers, workerIndex + 1, bikes, 
                    currDistanceSum + findDistance(workers[workerIndex], bikes[bikeIndex]));
                visited[bikeIndex] = false;
            }
        }
    }
    
    public int assignBikes(int[][] workers, int[][] bikes) {
        minimumDistanceSum(workers, 0, bikes, 0);
        return smallestDistanceSum;
    } 
}
