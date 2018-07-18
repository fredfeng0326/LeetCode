class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ret = 0
        last_bit = None
        bit = 0
        while N:
            if N & 1:
                if last_bit is not None:
                    ret = max(ret, bit - last_bit)
                last_bit = bit
            N >>= 1
            bit += 1
        return ret

a = Solution()
print (a.binaryGap(5))