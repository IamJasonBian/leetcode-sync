
class Solution {
    public List<String> mostVisitedPattern(String[] username, int[] timestamp, String[] website) {
        int n = username.length;

        Map<String,List<Pair<Integer,String>>> map = new HashMap<>();

        for(int i=0; i<n; i++) {
            String user = username[i];
            List<Pair<Integer,String>> curlist = map.getOrDefault(user, new ArrayList<>());
            Pair<Integer,String> pair = new Pair(timestamp[i],website[i]);
            curlist.add(pair);
            map.put(user,curlist);
        }

        // generate scores
        Map<String,Integer> mapScores = new HashMap<>();

        for(String user: map.keySet()) {
            List<Pair<Integer,String>>  curlist = map.get(user);
            Collections.sort(curlist, new Comparator<Pair<Integer, String>>() {
                @Override
                public int compare(Pair<Integer, String> a, Pair<Integer, String> b) {
                    return a.getKey() - b.getKey();
                }
            });
            List<String> newlist = new ArrayList<>();
            
            for(Pair<Integer,String> pair: curlist) {
                newlist.add(pair.getValue());
            }
            generateScore(newlist,mapScores);
        }

        // find the biggest score
        String maxScoreString = "";
        int maxScore = 0;
        for(String key: mapScores.keySet()) {
            if(mapScores.get(key) > maxScore || (mapScores.get(key) == maxScore && key.compareTo(maxScoreString)<0)) {
                maxScoreString = key;
                maxScore = mapScores.get(key);
            }
        }
        String[] strs = maxScoreString.split(",");
        List<String> result = new ArrayList<>();
        Collections.addAll(result, strs);

        return result;
    }

    public void generateScore(List<String> list, Map<String,Integer> mapScores ) {
        Set<String> set = new HashSet<>();
        int n = list.size();
        if(n<3) return;
        for(int i=0; i<n-2; i++) {
            for(int j=i+1; j<n-1; j++) {
                for(int k=j+1; k<n; k++) {
                    StringBuffer sb = new StringBuffer();
                    sb.append(list.get(i));
                    sb.append(",");
                    sb.append(list.get(j));
                    sb.append(",");
                    sb.append(list.get(k));
                    String str = sb.toString();
                    if(set.contains(str)) continue;
                    mapScores.put(str, mapScores.getOrDefault(str, 0)+1);
                    set.add(str);
                }
            }
        }
    }
}
