# You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.
# Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

# A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
# A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
# We drop one ball at the top of each column of the box. 
# Each ball can get stuck in the box or fall out of the bottom. 
# A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

# Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom 
# after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.

class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        '''
        1: go right
        -1: go left
        i: 1 and (i+1: -1 or i == len-1) => -1
        i: -1 and (i-1: 1 or i == 0) => -1
        '''
        pos = [i for i in range(0, len(grid[0]))]
        for layer in grid:
            memo = {}
            for i in range(len(pos)):
                if pos[i] == -1:
                    continue
                elif pos[i] in memo:
                    pos[i] = memo[pos[i]]
                if layer[pos[i]] == 1 and (pos[i]+1 >= len(pos) or layer[pos[i]+1] == -1):
                    pos[i] = -1
                    memo[pos[i]] = -1
                elif layer[pos[i]] == -1 and (pos[i]-1 < 0 or layer[pos[i]-1] == 1):
                    pos[i] = -1
                    memo[pos[i]] = -1
                else:
                    tmp = pos[i] + layer[pos[i]]
                    memo[pos[i]] = tmp
                    pos[i] = tmp
        
        return pos
