#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        res = 0
        arr.sort()
        for i in range(len(arr)//2):
            res += abs(arr[i] - arr[len(arr)-i-1])
        return res*2

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends