#User function Template for python3

class Solution:
    def __init__(self):
        self.result = []

    def IsSafe(self, board, row, col,n):
        for i in range(col):
            if board[row][i]:
                return False
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1
        i = row
        j = col
        while j >= 0 and i < n:
            if board[i][j]:
                return False
            i += 1
            j -= 1
        return True

    def solve(self, board, col, n):
        if col == n:
            v = []
            for i in board:
                for j in range(len(i)):
                    if i[j] == 1:
                        v.append(j + 1)
            self.result.append(v)
            return True

        res = False
        for i in range(n):
            if self.IsSafe(board, i, col,n):
                board[i][col] = 1
                res = self.solve(board, col + 1, n) or res
                board[i][col] = 0
        return res

    def nQueen(self, n):
        board = [[0 for i in range(n)] for j in range(n)]
        self.solve(board, 0, n)
        self.result.sort()
        return self.result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends