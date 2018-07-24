# 812. Largest Triangle Area
import itertools
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # S=(1/2)*(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)
        def size(p1,p2,p3):
            (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

        return max(size(a, b, c) for a, b, c in itertools.combinations(points, 3))

a = Solution()
print(a.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))