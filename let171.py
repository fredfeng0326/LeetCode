# 171. Excel Sheet Column Number
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenth = len(s)
        ans = 0
        for item in range(lenth):
            ans = ans + ((ord(s[lenth-item-1])-64)*(26**item))
        return ans
a = Solution()
print(a.titleToNumber("ZY"))

