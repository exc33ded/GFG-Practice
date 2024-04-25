#User function Template for python3

class Solution:
	def FindExitPoint(self, n, m, matrix):
		# Code here
		directions={
        'r':'d',
        'd':'l',
        'l':'u',
        'u':'r'
        }
        i,j=0,0
        move='r'
        m,n=len(matrix),len(matrix[0])
        while i<m and j<n and i>=0 and j>=0:
            if matrix[i][j]==0:
                if move=='r':
                    j+=1
                elif move=='l':
                    j-=1
                elif move=='d':
                    i+=1
                elif move=='u':
                    i-=1
            else:
                matrix[i][j]=0
                move=directions[move]
        if i>=m:
            i-=1
        if i<0:
            i+=1
        if j>=n:
            j-=1
        if j<0:
            j+=1
        return [i,j]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends