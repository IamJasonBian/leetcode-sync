class Solution:
    allprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
    def gcdSort(self, nums: List[int]) -> bool:
        def factorization(a):
            res = set([])
            for p in self.allprimes:
                if p > sqrt(a)+2:break
                while a % p == 0:
                    res.add(p)
                    a = a // p
            if a > 1: res.add(a)
            return res
        
        p = [i for i in range(len(nums))]
        def find(x):
            if x!=p[x]:
                p[x] = find(p[x])
            return p[x]

        ptoi = {}
        for i,a in enumerate(nums):
            factors = factorization(a)
            for prime in factors:
                if prime not in ptoi:
                    ptoi[prime] = i
                else:
                    j = ptoi[prime]
                    pi,pj = sorted([find(i),find(j)])
                    p[pj] = pi
        
        cates = [find(i) for i in range(len(nums))]

        sublist = {}
        indinc = []
        for i,a in enumerate(nums):
            subcat = cates[i]
            if subcat not in sublist:
                sublist[subcat] = []
            sublist[subcat].append(a)
            indinc.append(len(sublist[subcat])-1)
        
        for subcat in sublist:
            sublist[subcat].sort()
        sortednums = sorted(nums)
        for i,a in enumerate(nums):
            subcat = cates[i]
            sorteda = sublist[subcat][indinc[i]]
            if sublist[subcat][indinc[i]]!=sortednums[i]:
                return False
        return True

            





