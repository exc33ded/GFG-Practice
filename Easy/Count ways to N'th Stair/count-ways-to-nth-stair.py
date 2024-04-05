#User function Template for python3


class Solution:

    #Function to count number of ways to reach the nth stair
    #when order does not matter.
    def countWays(self, m):

        mod = 1000000007
        # code here
        if m == 0:            
            return 0
            
        elif m ==1:
            
            return 1        

        n1 = 1

        n2 = 2

        for _ in range(3, m+1):

            n1, n2  =  n2,  (n1+1)% mod
            
        return n2



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
        ob = Solution()
        print(ob.countWays(n))

# } Driver Code Ends