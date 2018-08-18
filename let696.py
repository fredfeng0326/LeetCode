# 696. Count Binary Substrings
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = [1]
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                groups[-1] += 1
            else:
                groups.append(1)
        ans = 0
        for i in range(0,len(groups)-1):
            ans += min(groups[i],groups[i+1])
        return ans




a = Solution()
print(a.countBinarySubstrings("00110011"))
