class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        List<String> ans = new ArrayList<>();

        Set<String> set = new HashSet<>();
        for(String st : wordDict){
            set.add(st);
        }
        String str = "";
        helper(s,set,0,0,ans,str);
        return ans;
        
    }

    void helper(String s, Set<String> set, int startIndex, int endIndex, List<String> ans, String str){
        if(endIndex == s.length()){
            if(startIndex == endIndex){
                ans.add(str);
                System.out.println(str);
            }
            
            return;
        }

        if(findMeaningfullWord(startIndex,endIndex,set,s)){
            if(startIndex == 0){
                str = str + s.substring(startIndex,endIndex+1);
                helper(s,set,endIndex+1,endIndex+1,ans,str);
                str = "";
            }else{
                int len = str.length();
                str = str + " " + s.substring(startIndex,endIndex+1);
                
                helper(s,set,endIndex+1,endIndex+1,ans,str);
                str = str.substring(0,len);
            }
        }

        helper(s,set,startIndex,endIndex+1,ans,str);

        return;
    }


    boolean findMeaningfullWord(int startIndex,int endIndex, Set<String> set, String s){
        String substr = s.substring(startIndex,endIndex+1);

        if(set.contains(substr)){
            return true;
        }
        return false;
    }
}
