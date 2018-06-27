# 806. Number of Lines To Write String
class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line_words = 0
        lines = 1
        for word in S:
            word_length = widths[ord(word)-97]
            line_words = word_length + line_words
            if line_words > 100:
                line_words = word_length
                lines +=1
            print (line_words)
        return [lines,line_words]

a = Solution()
print (a.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],'abcdefghijklmnopqrstuvwxyz'))