class Solution {
    public String alienOrder(String[] words) {
        HashMap<Character,List<Character>> hm = new HashMap<>();
        Map<Character,Integer> indegree = new HashMap<>();

        // Put every char initial indegree as 0
        for(int i=0;i<words.length;i++){
            for(int j=0;j<words[i].length();j++){
                indegree.put(words[i].charAt(j),0);
            }
        }

        for(int i=0;i<words.length-1;i++){
            String s1 = words[i];
            String s2 = words[i+1];
            if(s1.length()>s2.length() && s1.startsWith(s2)) return "";

            for(int p=0,q=0;p< s1.length() && q<s2.length();p++,q++){
                if(s1.charAt(p)!=s2.charAt(q)){
                    if(!hm.containsKey(s1.charAt(p))){
                        hm.put(s1.charAt(p),new ArrayList<>());
                    }
                    hm.get(s1.charAt(p)).add(s2.charAt(q));
                    break;
                }
            }
        }

        for(Map.Entry<Character,List<Character>> e: hm.entrySet()){
            Character k = e.getKey();
            List<Character> v = e.getValue();

            for(int i=0;i<v.size();i++){
                indegree.put(v.get(i),indegree.get(v.get(i)) +1);
            }
        }

        Queue<Character> q = new LinkedList<>();

        for(Map.Entry<Character,Integer> e: indegree.entrySet()){
            if(e.getValue() == 0) q.add(e.getKey());
        }

        StringBuilder sb = new StringBuilder();

        while(!q.isEmpty()){
            Character ch = q.poll();
            sb.append(ch);
            List<Character> l = hm.get(ch);
            if(l == null || l.size()==0) continue;

            for(char c : l){
                indegree.put(c,indegree.get(c)-1);
                if(indegree.get(c) == 0){
                    q.add(c);
                }
            }

        }

        if(sb.length() ==  indegree.size()) return sb.toString();

        return "";
    }
}
