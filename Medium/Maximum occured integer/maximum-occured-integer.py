#User function Template for python3

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,N, L, R, maxx):
        ##Your code here
        helperArr = [0] * (maxx+2)
        
        # Exec queries
        for i in range(0, N):
            helperArr[L[i]] = helperArr[L[i]] + 1
            helperArr[ R[i]+1 ] = helperArr[ R[i]+1 ] - 1
        
        # Prefix sum 
        for i in range(1, len(helperArr)):
            helperArr[i] += helperArr[i-1]
        
        maxFreq =max(helperArr)
        return helperArr.index(maxFreq)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends