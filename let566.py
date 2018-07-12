# 566. Reshape the Matrix

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        len_1 = len(nums) * len(nums[0])
        len_2 = r * c
        list = []
        if len_1 != len_2:
            return nums
        else:
            for row in nums:
                for col in row:
                    list.append(col)
            newMatrix = [[0 for x in range(c)] for y in range(r)]
            for i in range(r):
                for j in range(c):
                    newMatrix[i][j] = list[i*c+j]
            return newMatrix


a = Solution()
print (a.matrixReshape([[1,2],[3,4]],r = 1, c = 4))