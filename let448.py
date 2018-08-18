class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums) + 1)) - set(nums))

a = Solution()
print(a.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(set(range(1,6)))