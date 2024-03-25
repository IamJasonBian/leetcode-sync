class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(100000)
        ans=''
        n=[]
        List1=map(str, num)
        for char in List1:
            ans=ans+char

        Sum=int(ans)
        final=Sum+k

        a=str(final)
        for char in a:
            n.append(char)

        n=map(int, n)
        return n

            
        
