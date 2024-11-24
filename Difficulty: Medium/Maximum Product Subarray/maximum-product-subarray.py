#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr):
        n = len(arr)
        # code here
        prefix_sum = 1
        suffix_sum = 1
        max_ = arr[0]
        
        for i in range(n):
            if prefix_sum == 0:
                prefix_sum = 1
                
            if suffix_sum == 0:
                suffix_sum = 1
            
            prefix_sum *= arr[i]
            suffix_sum *= arr[n - i - 1]
            
            max_ = max(max_, max(prefix_sum, suffix_sum))
            
        return max_




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends