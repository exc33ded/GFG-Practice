#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
        MOD = 10**9 + 7
        if n == 1:
            return 0
        dp = [[0]*2 for _ in range(n+1)]
        # Base cases
        dp[1][0] = 1
        dp[1][1] = 1
        for i in range(2, n+1):
            dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
            dp[i][1] = dp[i-1][0] % MOD
        total_valid_strings = (dp[n][0] + dp[n][1]) % MOD
        total_strings = pow(2, n, MOD)
        answer = (total_strings - total_valid_strings + MOD) % MOD
        return answer
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends