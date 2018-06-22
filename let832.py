# 832. Flipping an Image


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rlist = []
        for item in A:
            # new_item = item[::-1]
            item.reverse()
            for n,element in enumerate(item):
                if element == 0:
                    item[n] = 1
                else:
                    item[n] = 0
            rlist.append(item)
        return rlist


a = Solution()
print(a.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(a.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))