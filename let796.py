# 796. Rotate String
class Solution:
    def rotateString1(self, A, B):
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        for s in range(len(A)):
            if all(A[(s + i) % len(A)] == B[i] for i in range(len(A))):
                return True
        return False

    def rotateString2(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and B in A + A



a = Solution()
print(a.rotateString2('abcde','cdeab'))