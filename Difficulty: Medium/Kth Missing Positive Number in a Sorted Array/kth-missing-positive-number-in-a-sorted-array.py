#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        n = len(arr)
        for i in range(n):
            if arr[i] > (k + i):
                return k + i

        return k + n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends