class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for string in ops:
            if string == 'C':
                stack.pop()
            elif string == 'D':
                if stack:
                    stack.append(stack[-1] * 2)
            elif string == '+':
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(string))

        return sum(stack)

a = Solution()
print (a.calPoints(["5","2","C","D","+"]))