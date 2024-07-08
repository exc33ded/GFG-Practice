#User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest (self, arr, target):
    # Your Code Here
        arr.sort()
        n = len(arr)
        min_delta = float("inf")
        
        for i in range(n-1, 1, -1):
            right = i - 1
            left = 0
            while left < right:
                csum = arr[i] + arr[left] + arr[right]
                delta = abs(csum - target)
                if delta < min_delta:
                    min_delta = delta
                    msum = csum
                elif delta == min_delta:
                    msum  = max(csum, msum)
                if csum < target:
                    left += 1
                else:
                    right -= 1
        return msum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.threeSumClosest(A, k))

# } Driver Code Ends