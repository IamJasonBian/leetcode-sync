class Solution {
    public int[][] reconstructQueue(int[][] people) {
     ArrayList<int[]> list = new ArrayList<>();
        int n=people.length;
        Arrays.sort(people,(a,b)->{
            if(a[0]!=b[0])
                return b[0]-a[0];
            return a[1]-b[1];
        });
           int[][] res = new int[n][2];
         int i=0;
        for(int[] a:people){
            list.add(a[1],a);
          
        }
      
       
        for(int[] a: list){ 
            res[i]=a;
         //   System.out.println(list.get(a[1])[0]+""+ list.get(a[1])[1]);
            i++;
                     
        }
        
        return res;
        
    }
}
