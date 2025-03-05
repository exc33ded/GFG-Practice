class Solution:
    def lcs(self, s1, s2):
        # code here
        m, n = len(s1), len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[-1][-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s1 = str(input())  # Take first string as input
        s2 = str(input())  # Take second string as input
        ob = Solution()
        # Call the lcs function and print the result
        print(ob.lcs(s1, s2))
        print("~")

# } Driver Code Ends