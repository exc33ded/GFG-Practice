#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        n = len(arr)
        if n == 0:
            return 0
        
        max_steps = 0
        cur_steps = 0
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                cur_steps += 1
            else:
                cur_steps = 0
            max_steps = max(max_steps, cur_steps)
        
        return max_steps
            
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends