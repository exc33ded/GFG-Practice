
from typing import List


class Solution:
    def minimizeDifference(self, n: int, k: int, arr: List[int]) -> int:
        maxSuffix = [-float('inf')] * (n + 1)
        minSuffix = [float('inf')] * (n + 1)
        
        maxSuffix[n] = -float('inf')
        minSuffix[n] = float('inf')
        
        # Calculate suffix maximums and minimums
        maxSuffix[n - 1] = arr[n - 1]
        minSuffix[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            maxSuffix[i] = max(maxSuffix[i + 1], arr[i])
            minSuffix[i] = min(minSuffix[i + 1], arr[i])
        
        # Initialize prefix maximum and minimum values
        maxPrefix = arr[0]
        minPrefix = arr[0]
        
        # Initialize the minimum difference with the maximum and minimum values of the first k elements
        minDiff = maxSuffix[k] - minSuffix[k]
        
        # Iterate through the array to find the minimum difference
        for i in range(1, n):
            # Check if the window size doesn't exceed the array size
            if i + k <= n:
                # Update maximum and minimum values considering the current prefix and the next k elements
                maxi = max(maxSuffix[i + k], maxPrefix)
                mini = min(minSuffix[i + k], minPrefix)
                # Update the minimum difference if a smaller difference is found
                minDiff = min(minDiff, maxi - mini)
            # Update prefix maximum and minimum values
            maxPrefix = max(maxPrefix, arr[i])
            minPrefix = min(minPrefix, arr[i])
        
        # Return the minimum difference
        return minDiff


#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.minimizeDifference(n, k, arr)
        
        print(res)
        

# } Driver Code Ends