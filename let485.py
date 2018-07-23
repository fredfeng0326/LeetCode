# 485. Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ''.join(str(i) for i in nums)
        list =  s.split('0')
        return max([len(item) for item in list])


a = Solution()
print(a.findMaxConsecutiveOnes([1,1,0,1,1,1]))
