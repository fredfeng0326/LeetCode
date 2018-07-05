# 500. Keyboard Row

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        list1 = {'q','w','e','r','t','y','u','i','o','p'}
        list2 = {'a','s','d','f','g','h','j','k','l'}
        list3 = {'z','x','c','v','b','n','m'}
        list = []
        for item in words:
            item2 = item.lower()
            if (set(item2).issubset(list1) or set(item2).issubset(list2) or set(item2).issubset(list3)):
                list.append(item)
        return list

a = Solution()
print(a.findWords(["Hello", "Alaska", "Dad", "Peace"]))