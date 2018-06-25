# 461. Hamming Distance
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')


a = Solution()
print (a.hammingDistance(1,4))