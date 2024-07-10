from typing import List


class Solution:
    def MaxConnection(self, grid : List[List[int]]) -> int:
        # code here
        if(len(grid) == 1):
            return 1
        def findMax(a, grid, i, j):
            if(i==len(grid) or j==len(grid) or i<0 or j<0):
                return a
            if(grid[i][j] == 1):
                a.append([i,j])
                grid[i][j] = -1
                a = findMax(a, grid, i, j+1)
                a = findMax(a, grid, i, j-1)
                a = findMax(a, grid, i+1, j)
                a = findMax(a, grid, i-1, j)
            return a
        
        def checkIf(x,grid):
            if(x[0]>=len(grid) or x[1]>=len(grid) or x[0]<0 or x[1]<0):
                return False
            if grid[x[0]][x[1]]==0:
                return False
            return True
            
        
        myDict = {}
        m= 0;
        
        for i in range(0,len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 1):
                    temp = findMax([], grid, i, j)
                    m = max(m, (len(temp)))
                    if(len(temp)>0):
                        for index in temp:
                            # print(index)
                            myDict[index[0], index[1]] = temp[0]
                            grid[index[0]][index[1]] = len(temp)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 0):
                    newl = [[i+1, j], [i, j+1], [i, j-1], [i-1, j]]
                    li = []
                    ma = 0
                    for x in newl:
                        if(checkIf(x,grid) and myDict[x[0], x[1]] not in li):
                            li.append(myDict[x[0], x[1]])
                            ma = ma + grid[x[0]][x[1]]
                    m = max(m, ma+1)
        
        
        return m
        



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

        n = int(input())

        grid = IntMatrix().Input(n, n)

        obj = Solution()
        res = obj.MaxConnection(grid)

        print(res)

# } Driver Code Ends