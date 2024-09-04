#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        # code here
        original_sum = n * (n + 1)//2
        produced_sum = sum(arr)
        return abs(original_sum - produced_sum)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends