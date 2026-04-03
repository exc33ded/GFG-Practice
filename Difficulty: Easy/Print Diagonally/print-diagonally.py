
from itertools import chain
class Solution:
        
    def diagView(self, mat): 
        
        res = [[] for _ in range(2 * n - 1)]
        
        for i in range(n):
            for j in range(n):
                res[i+j].append(mat[i][j])

        return list(chain.from_iterable(res))