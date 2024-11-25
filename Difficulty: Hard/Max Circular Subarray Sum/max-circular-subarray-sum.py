#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    n = len(arr)
    def kadane(arr):
        max_sum = arr[0]
        curr_sum = arr[0]
        for num in arr[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

    # Case 1: Maximum sum subarray is non-circular
    max_non_circular = kadane(arr)

    # Case 2: Maximum sum subarray is circular
    total_sum = sum(arr)
    arr_neg = [-x for x in arr]
    max_circular = total_sum + kadane(arr_neg)
    
    if max_circular == 0:  # all elements are negative
        return max_non_circular
    
    return max(max_non_circular, max_circular)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends