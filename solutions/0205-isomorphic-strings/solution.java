import java.util.HashMap;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false; // Strings must be of the same length to be isomorphic
        }
        
        HashMap<Character, Character> sToT = new HashMap<>();
        HashMap<Character, Character> tToS = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char sc = s.charAt(i);
            char tc = t.charAt(i);
            
            if ((sToT.containsKey(sc) && sToT.get(sc) != tc) || (tToS.containsKey(tc) && tToS.get(tc) != sc)) {
                return false; // Mapping is not bijective
            }
            
            sToT.put(sc, tc);
            tToS.put(tc, sc);
        }
        
        return true; // All characters are isomorphically mapped
    }
}

