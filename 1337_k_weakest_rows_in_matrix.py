# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). 
# The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.

# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weak_rank = sorted([(sum(row), i) for i, row in enumerate(mat)])
        return [weak_rank[i][1] for i in range(k)]
