# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

class Solution:
    def exist(self, board, word):
        r_len = len(board)
        c_len = len(board[0])
        
        def search_next(r,c,i,used):
            if i >= len(word) and len(used) == len(word):
                return True
            print(f'({r},{c})', f'({i},{word[i]})', used)
            
            candidates = []
            if r < r_len-1 and (r+1,c) not in used and board[r+1][c] == word[i]:
                candidates.append((r+1,c))
            if r > 0 and (r-1,c) not in used and board[r-1][c] == word[i]:
                candidates.append((r-1,c))
            if c < c_len-1 and (r,c+1) not in used and board[r][c+1] == word[i]:
                candidates.append((r,c+1))
            if c > 0 and (r,c-1) not in used and board[r][c-1] == word[i]:
                candidates.append((r,c-1))
            
            if len(candidates) == 0:
                return False
            
            for next_pos in candidates:
                used.append((next_pos[0],next_pos[1]))
                if search_next(next_pos[0], next_pos[1], i+1, used):
                    return True
                else:
                    used.pop()
            
        for row in range(r_len):
            for col in range(c_len):
                print(f'row={row}, col={col}, {board[row][col]}')
                if board[row][col] == word[0] and search_next(row, col, 1, [(row,col)]):
                    return True
        return False

class Solution_0:
    def exist1(self, board, word):
        N_ROWS = len(board)
        N_COLS = len(board[0])
        N_WORD = len(word)
        
        path = set()
        def dfs(r, c, i):
            if i == N_WORD:
                return True
            
            if (not (0 <= r < N_ROWS) or
                not (0 <= c < N_COLS) or
                (word[i] != board[r][c]) or
                ((r, c) in path)):
                return False
            
            path.add((r, c))
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            path.remove((r, c))
            return res
        
        for r in range(N_ROWS):
            for c in range(N_COLS):
                if dfs(r, c, 0):
                    return True
        return False
            
    def exist(self, board, word):
        board_x, board_y = len(board), len(board[0])
        word_len = len(word)
        
        flatten = lambda y: [x for a in y for x in flatten(a)] if type(y) is list else [y]
        board_flat = flatten(board)
        
        # return False if we don't have enough letters in board for word
        for letter in tuple(set(word)):
            if board_flat.count(letter) < word.count(letter):
                return False
        
        # reverse the word if last letter of it has less occurences in board
        # so we will start less initial recursions
        if board_flat.count(word[-1]) < board_flat.count(word[0]):
            word = word[::-1]
        
        # add a frame around the board as a path,
        # to mark the no-go zone for algorithm
        path = set()
        for i in range(-1, board_x + 1):
            path.add((i, -1))
            path.add((i, board_y))
        for j in range(board_y):
            path.add((-1, j))
            path.add((board_x, j))            
        
        def dfs(i: int, j: int, k: int) -> bool:
            
            if (i, j) in path:
                return False
            
            if board[i][j] != word[k]:
                return False
            
            kk = k+1
            if kk == word_len:
                return True
            
            path.add((i, j))

            if dfs(i, j+1, kk) or dfs(i+1, j, kk) or dfs(i, j-1, kk) or dfs(i-1, j, kk):
                return True
                
            path.remove((i, j))
            return False
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
                
        return False
                    
if __name__ == '__main__':
    sol = Solution()
    print(sol.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))
