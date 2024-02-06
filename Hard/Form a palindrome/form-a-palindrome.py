#User function Template for python3

class Solution:
    def countMin(self, Str):
        # code here
        if Str == Str[::-1]:
            return 0
        n = len(Str)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n - 1):
            if Str[i] == Str[i + 1]:
                dp[i][i + 1] = 0
            else:
                dp[i][i + 1] = 1
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                if Str[i] == Str[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n - 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        

        solObj = Solution()

        print(solObj.countMin(Str))
# } Driver Code Ends