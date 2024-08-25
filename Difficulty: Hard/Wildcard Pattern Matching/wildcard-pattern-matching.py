# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    def wildCard(self, pattern, string):
        n = len(string)
        m = len(pattern)

        # Create a DP table to store the results of subproblems
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Empty pattern matches empty string
        dp[0][0] = True

        # Handle patterns with '*' at the beginning
        for j in range(1, m + 1):
            if pattern[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Build the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if pattern[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif pattern[j - 1] == '?' or string[i - 1] == pattern[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[n][m]



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)

# } Driver Code Ends