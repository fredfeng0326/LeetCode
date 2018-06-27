# 561. Array Partition I
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])

a = Solution()
print (a.arrayPairSum([1,4,3,2]))