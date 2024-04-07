#User function Template for python3


#Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self,n, arr):
        # code here
        memo = {}
        def solve(i, j):
            if i > j or i >= n or j < 0:
                return 0
            k = (i, j)
            if k in memo:
                return memo[k]
            option1 = arr[i] + min(solve(i+2, j), solve(i+1, j-1))
            option2 = arr[j] + min(solve(i+1, j-1), solve(i, j-2))
            memo[k] = max(option1, option2)
            return memo[k]
        return solve(0, n-1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(n,arr))

# } Driver Code Ends