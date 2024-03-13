# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        n , res = len(mat), []
        for i in range(2*n - 1):
            extra = i - n + 1
            if i % 2 == 0:
                row , col = i if extra <= 0 else n - 1, 0 if extra <= 0 else extra
                while row >= 0 and col < n:
                    res.append(mat[row][col])
                    row, col = row - 1, col + 1
            else:
                row , col = 0 if extra <= 0 else extra, i if extra <= 0 else n - 1
                while row < n and col >= 0:
                    res.append(mat[row][col])
                    row, col = row + 1, col - 1
        return res


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends