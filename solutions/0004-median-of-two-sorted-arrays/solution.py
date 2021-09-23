class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def mergeArrays(nums1, nums2, n1, n2):
            nums3 = [None] * (n1 + n2)
            i = 0
            j = 0
            k = 0
            
            #Traverse both arrays
            while i < n1 and j < n2:
                if nums1[i] < nums2[j]:
                    nums3[k] = nums1[i]
                    #initialized post-merged array
                    k = k + 1
                    i = i + 1
                else:
                    nums3[k] = nums2[j]
                    k = k + 1
                    j = j + 1
            
            #increment counters after selecting which one to merge
            while i < n1:
                nums3[k] = nums1[i]
                k = k + 1
                i = i + 1
            
            while j <n2:
                nums3[k] = nums2[j]
                k = k + 1
                j = j + 1
            return(nums3)
                
        n1 = len(nums1)
        n2 = len(nums2)
        
        num3 =  mergeArrays(nums1, nums2, n1, n2)
        
        def median(l):
            half = len(l) // 2
            if not len(l) % 2:
                return (l[half - 1] + l[half]) / 2.0
            return l[half]
        
        return(median(num3))
        
        
            
                
