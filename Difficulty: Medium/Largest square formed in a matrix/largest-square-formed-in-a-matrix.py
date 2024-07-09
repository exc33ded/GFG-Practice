
from typing import List


class Solution:
    def maxSquare(self, n, m, mat):
        largest = [[0 for _ in range(m)] for _ in range(n)]
        
        # setting up bottom and left borders
        maxSize = 0
        #bottom
        for i in range(m):
            largest[-1][i] = mat[-1][i]
            maxSize = max(maxSize,largest[-1][i])
        
        #left
        for i in range(n):
            largest[i][-1] = mat[i][-1]
            maxSize = max(maxSize,largest[i][-1])
            
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if mat[j][i]==1:
                    largest[j][i] = 1 + min(largest[j+1][i],largest[j][i+1],largest[j+1][i+1])
                    maxSize = max(maxSize,largest[j][i])
        
        return maxSize
        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n, m = map(int, input().split())

        mat = IntMatrix().Input(n, m)

        obj = Solution()
        res = obj.maxSquare(n, m, mat)

        print(res)

# } Driver Code Ends