class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        if word[0].isupper():
            if word[1:].isupper() or word[1:].islower():
                return True
            else:
                return False
        if word[0].islower():
            if word[1:].islower():
                return True
            else:
                return False

a = Solution()
print(a.detectCapitalUse('Leetcode'))

print ('Leetcode'[1:].islower())
