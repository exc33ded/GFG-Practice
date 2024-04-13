#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def printArr(self, n, arr):
        # printing array elements with spaces
        print(*arr)

    def setToZero(self, n, arr):
        # setting all elements to zero
        for i in range(len(arr)):
            arr[i] = 0
        
    def xor1ToN(self, n, arr):
        # doing xor with indices
        for i in range(len(arr)):
            arr[i] = arr[i] ^ i
            

#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        obj = Solution()
        obj.xor1ToN(n, arr)
        obj.printArr(n, arr)
        obj.setToZero(n, arr)
        obj.printArr(n, arr)

# } Driver Code Ends