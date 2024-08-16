#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        result = [1] * n
        
        # First pass: Calculate products of all elements to the left of each index
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # Second pass: Calculate products of all elements to the right of each index
        # and multiply with the left product in the result array
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends