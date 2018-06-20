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

    def numJewelsInStones2(self,J,S):
        return sum(s in J for s in S)

a = Solution()
print (a.numJewelsInStones('aA','aAAbbbb'))
print (a.numJewelsInStones2('aA','aAAbbbb'))