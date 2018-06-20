class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        i = 0
        for Jitem in J:
            for Sitem in S:
                if Jitem == Sitem:
                    i += 1
        return i

a = Solution()
print (a.numJewelsInStones('aA','aAAbbbb'))