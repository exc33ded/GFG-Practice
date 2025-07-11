class Solution:
    def maxGold(self, mat):
        # code here
        m, n = len(mat), len(mat[0])
        for c in range(1, n):
            for r in range(m):
                v = mat[r][c-1]
                v = max(v, mat[r-1][c-1]) if r-1 >= 0 else v
                v = max(v, mat[r+1][c-1]) if r+1 < m else v
                mat[r][c] += v
        return max(mat[r][-1] for r in range(m))