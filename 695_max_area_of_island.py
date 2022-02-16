# You are given an m x n binary matrix grid. 
# An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        height = len(grid)
        width = len(grid[0])
        
        def find_neighbors(r, c, q):
            area = 0
            
            # up
            if r > 0 and grid[r-1][c]:
                q.append((r-1,c))
                grid[r-1][c] = 0
                area += 1
            # down
            if r < height-1 and grid[r+1][c]:
                q.append((r+1,c))
                grid[r+1][c] = 0
                area += 1
            # left
            if c > 0 and grid[r][c-1]:
                q.append((r,c-1))
                grid[r][c-1] = 0
                area += 1
            # right
            if c < width-1 and grid[r][c+1]:
                q.append((r,c+1))
                grid[r][c+1] = 0
                area += 1
            
            return area
        
        for r in range(height):
            for c in range(width):
                if grid[r][c] == 1:
                    q = deque()
                    q.append((r, c))
                    grid[r][c] = 0
                    area = 1
                    
                    while q:
                        x, y = q.popleft()
                        area += find_neighbors(x, y, q)
                    
                    max_area = max(max_area, area)
        
        return max_area
