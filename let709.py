# 709. To Lower Case

class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

    def toLowerCase2(self, str):
        """
        :type str: str
        :rtype: str
        """
        # return [chr(ord(i) + 32) for i in str if 65 <= ord(i) <= 90]
        result = ''
        for i in str:
            index = ord(i)
            if 65 <= index <= 90:
                result += chr(index + 32)
            else:
                result += i
        return result

a = Solution()
print(a.toLowerCase2('Hello'))