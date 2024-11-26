#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        arr=set(arr)
        m=999999
        for i in arr:
            if i>=0 and i+1 not in arr:
                m=min(i+1,m)
        if 1 not in arr:
            return 1
        else:
            return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends