class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lis=[]
        arr=[i for i in range(1,n+1)]

        def sequences(i,lis,arr,n,k,ans=[]):
            if i==n:
                if len(lis)==k:
                    # print(lis)
                    ans.append(lis.copy())
                return
            
            lis.append(arr[i])
            sequences(i+1,lis,arr,n,k)
            lis.pop()
            
            sequences(i+1,lis,arr,n,k)

            return ans

        return sequences(0,lis,arr,n,k)

