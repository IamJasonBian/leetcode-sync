class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        ans=[]
        def factorsplit(n,factors,rem):
            if factors==0:
                if n==1:
                    ans.append(rem[:])
                return
            if factors>n:
                return
            for i in range(1,int(sqrt(n))+1):
                if n%i==0:
                    factorsplit(n//i,factors-1,rem+[i])
                    if i*i!=n:
                        factorsplit(i,factors-1,rem+[n//i])
        factorsplit(n,k,[])
        diff=float('inf')
        res=[]
        for i in ans:
            i.sort()
            curr=i[-1]-i[0]
            if curr<diff:
                diff=curr
                res=i 
        return res
