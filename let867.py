# matrix transpose
import numpy as np
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(map(list, zip(*A)))
    def transpose2(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(A), len(A[0])
        res = [[0] * rows for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                res[col][row] = A[row][col]
        return res

    def transpose3(self,A):
        return np.array(A).T.tolist()



a = Solution()
print (a.transpose([[1,2,3],[4,5,6],[7,8,9]]))
print (a.transpose2([[1,2,3],[4,5,6],[7,8,9]]))
print (a.transpose3([[1,2,3],[4,5,6],[7,8,9]]))