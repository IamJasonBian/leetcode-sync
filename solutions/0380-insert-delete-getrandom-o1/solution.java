class RandomizedSet {
    private HashMap<Integer,Integer> map=new HashMap<>();
    ArrayList<Integer> list=new ArrayList<>();

    public RandomizedSet() {
        map.clear();
        list.clear();
    }
    
    public boolean insert(int val) {
        if(map.containsKey(val)) return false;
        else{
            map.put(val,list.size());
            list.add(val);
            return true;
        }
    }
    
    public boolean remove(int val) {  
        if(!map.containsKey(val)) return false;
        else{
            int idxOfVal=map.get(val);
            int temp=list.get(list.size()-1); 
            list.set(list.size()-1,val); 

            list.set(idxOfVal,temp);     
            list.remove(list.size()-1); 
             
            map.put(temp,idxOfVal);
            map.remove(val);
            return true;
        }
    }
    
    public int getRandom() {
        int randomIdx = (int)(Math.random() * list.size());
        return list.get(randomIdx);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
