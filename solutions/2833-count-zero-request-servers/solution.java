import java.util.*;

class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        // Sort logs by time
        Arrays.sort(logs, Comparator.comparingInt(log -> log[1]));
        
        // Create and sort query indices based on query values
        Integer[] queryIndices = IntStream.range(0, queries.length)
            .boxed()
            .sorted(Comparator.comparingInt(i -> queries[i]))
            .toArray(Integer[]::new);
        
        int[] result = new int[queries.length];
        int[] activeRequests = new int[n + 1]; // Assuming server IDs are 1-based
        Deque<int[]> window = new ArrayDeque<>();
        int logIndex = 0;
        int availableServers = n;
        
        for (int idx : queryIndices) {
            int leftBound = queries[idx] - x;
            int rightBound = queries[idx];
            
            // Remove logs outside the left boundary
            while (!window.isEmpty() && window.peekFirst()[1] < leftBound) {
                int serverId = window.pollFirst()[0];
                activeRequests[serverId]--;
                if (activeRequests[serverId] == 0) {
                    availableServers++;
                }
            }
            
            // Add new logs within the right boundary
            while (logIndex < logs.length && logs[logIndex][1] <= rightBound) {
                int serverId = logs[logIndex][0];
                int time = logs[logIndex][1];
                
                if (time >= leftBound) {
                    window.addLast(logs[logIndex]);
                    if (activeRequests[serverId] == 0) {
                        availableServers--;
                    }
                    activeRequests[serverId]++;
                }
                logIndex++;
            }
            
            result[idx] = availableServers;
        }
        
        return result;
    }
    

    public static void main(String[] args) {
        Solution sol = new Solution();

        int n = 3;
        int[][] logs = {{1, 1}, {2, 3}, {1, 4}, {3, 5}};
        int x = 2;
        int[] queries = {2, 3, 4, 5};
        
        int[] result = sol.countServers(n, logs, x, queries);
        System.out.println("Results: " + Arrays.toString(result));
    }
}
