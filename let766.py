# 766. Toeplitz Matrix
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(matrix[row + 1][1:] == matrix[row][:-1] for row in range(len(matrix) - 1))

    def isToeplitzMatrix2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row in range(len(matrix) - 1):
            for col in range(len(matrix[0]) - 1):
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False
        return True




a = Solution()
print (a.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print (a.isToeplitzMatrix2([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))