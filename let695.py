# 695. Max Area of Island

class Solution:
    area = 0
    max = 0
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        for y in range(m):
            for x in range(n):
                self.area = 0
                if grid[y][x] == 1:
                    self.__dfs(grid, x, y, n, m)
        return self.max


    def __dfs(self,grid,x,y,n,m):
        if x<0 or y<0 or x >= n or y>=m or grid[y][x] == 0:
            return
        grid[y][x] = 0
        self.area = self.area +1
        self.__dfs(grid, x + 1, y, n, m)
        self.__dfs(grid, x - 1, y, n, m)
        self.__dfs(grid, x, y + 1, n, m)
        self.__dfs(grid, x, y - 1, n, m)
        if self.area > self.max:
            self.max = self.area

a = Solution()
print (a.numIslands([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))