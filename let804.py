import string
class Solution:
    s = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MoseList = []
        mylist = []
        for item in words:
            MoseString = ''
            for character in item:
                index = string.ascii_lowercase.index(character)
                MoseString += self.s[index]
            MoseList.append(MoseString)
            mylist = set(MoseList)
        return len(mylist)

    def uniqueMorseRepresentations2(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        moorse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        trans = lambda x: moorse[ord(x) - ord('a')]
        map_word = lambda word: ''.join([trans(x) for x in word])
        res = map(map_word, words)
        return len(set(res))

a = Solution()
print(a.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
print(a.uniqueMorseRepresentations2(["gin", "zen", "gig", "msg"]))