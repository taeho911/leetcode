'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:

  - Integers in each row are sorted from left to right.
  - The first integer of each row is greater than the last integer of the previous row.
'''

class Solution:
    def searchMatrix(self, matrix, target):
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        r_len = len(matrix)
        
        r_left = 0
        r_right = r_len - 1
        r = -1
        
        while r_left <= r_right:
            t = (r_left + r_right) // 2
            if target == matrix[t][0]:
                return True
            elif r_left == r_right:
                r = t
                break
            elif target < matrix[t][0]:
                r = t
                if t != 0 and target >= matrix[t-1][0]:
                    r = t-1
                    break
                r_right = t - 1
            elif target > matrix[t][0]:
                r = t
                if t != r_len - 1 and target < matrix[t+1][0]:
                    break
                r_left = t + 1
        return target in matrix[r]

class Solution_0:
    def searchMatrix(self, matrix, target):
        
        rows=len(matrix)
        cols=len(matrix[0])
        top,bottom=0,rows-1
        
        #if element not in the matrix range
        if target<matrix[top][0] or target>matrix[bottom][cols-1]:
            return False
        
        #finding the row 
        while top<=bottom:
            mid=(top+bottom)//2
            if target<matrix[mid][0]:
                bottom=mid-1
            elif target>matrix[mid][-1]:
                top=mid+1
            else:
                break
                                
        row=(top+bottom)//2
        left,right=0,cols-1
        
        #finding whether element is present in that row
        while left<=right:
            centre=(left+right)//2
            if target<matrix[row][centre]:
                right=centre-1
            elif target>matrix[row][centre]:
                left=centre+1
            else:
                return True
            
        return False
