class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        sp = list(moves)
        if (sp.count('R') == sp.count('L') and sp.count('U') == sp.count('D')):
            return True
        else:
            return False

    def judgeCircle2(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L') == moves.count('R') and moves.count('U') and moves.count('D')

a = Solution()
print (a.judgeCircle('LL'))
print (a.judgeCircle2('LL'))