#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        if N == 0:
            return 0

        max_sum = float('-inf')
        current_sum = 0

        for i in range(N):
            current_sum += arr[i]

            # Update max_sum if current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum

            # Reset current_sum to 0 if it becomes negative
            if current_sum < 0:
                current_sum = 0

        # If all elements are negative, return the maximum negative element
        if max_sum == float('-inf'):
            return max(arr)

        return max_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends