# 852. Peak Index in a Mountain Array

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low = 0
        high = len(A) - 1
        while low < high:
            middle = (low + high) // 2
            if A[middle] < A[middle + 1]:
                low = middle +1
            else:
                high = middle
        return low

a = Solution()
print (a.peakIndexInMountainArray([0,1,0]))