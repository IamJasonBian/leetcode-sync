import java.util.*;

  class Solution {
      public boolean validTree(int n, int[][] edges) {
          /*
              You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges
  where edges[i] = [a_i, b_i] indicates that there is an undirected edge between nodes a_i and b_i in the graph

              Return true if the edges of the given graph make up a valid tree, and false otherwise

              Initial Approach

                  * Traverse through the tree and check for each adjacent node if another node is pointed to it

                      * I.E. in [[0,1],[1,2],[2,3],[1,3],[1,4]]
                          * Both 2 and 1 points to 3 etc

                      * If an adjacent implementation is detected, return false

          */

          if (edges.length != n - 1) {
              return false;
          }

          Map<Integer, List<Integer>> adjacencyList = new HashMap<>();

          for (int[] edge : edges) {
              adjacencyList.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(edge[1]);
              adjacencyList.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(edge[0]);
          }

          System.out.println(Arrays.deepToString(edges));

          for (Map.Entry<Integer, List<Integer>> entry : adjacencyList.entrySet()) {
              System.out.println(entry.getKey() + " -> " + entry.getValue());
          }

          Set<Integer> visited = new HashSet<>();

          // Check for cycles starting from node 0
          if (hasCycle(0, -1, adjacencyList, visited)) {
              return false;
          }

          // Check if all nodes are connected
          if (visited.size() != n) {
              return false;
          }

          return true;
      }

      private boolean hasCycle(int node, int parent, Map<Integer, List<Integer>> adjacencyList, Set<Integer>
  visited) {
          visited.add(node);
          List<Integer> neighbors = adjacencyList.getOrDefault(node, new ArrayList<>());

          for (int neighbor : neighbors) {
              if (!visited.contains(neighbor)) {
                  if (hasCycle(neighbor, node, adjacencyList, visited)) {
                      return true;
                  }
              } else if (neighbor != parent) {
                  return true;
              }
          }
          return false;
      }


    
    



  }
