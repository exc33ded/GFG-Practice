#User function Template for python3

class Solution:
    def numberOfPath (self, n, k, arr):
        # code here
        def util(i,j,k):
            if i==n-1 and j==n-1 and k==arr[i][j]:
                return 1
            if i>=n or j>=n or k<0:
                return 0
            if dp[i][j][k]!=-1:
                return dp[i][j][k]
            down=util(i+1,j,k-arr[i][j])
            right=util(i,j+1,k-arr[i][j])
            dp[i][j][k]=down+right
            return dp[i][j][k]
        
        dp=[[[-1 for _ in range(k+1)]for _ in range(n+1)]for _ in range(n+1)]
        return util(0,0,k)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        k= int(input())
        n=int(input())
        l = list(map(int, input().split()))
        arr = list()
        c=0
        for i in range(0, n):
            temp = list()
            for j in range(0, n):
                temp.append(l[c])
                c += 1
            arr.append(temp)
        ans = ob.numberOfPath(n, k, arr);
        print(ans)


# } Driver Code Ends