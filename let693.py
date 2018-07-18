# 693. Binary Number with Alternating Bits
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = n & 1
        n >>= 1
        while n :
            if last == (n & 1):
                return False
            last = n & 1
            n >>= 1
        return True

a = Solution()
print (a.hasAlternatingBits(5))