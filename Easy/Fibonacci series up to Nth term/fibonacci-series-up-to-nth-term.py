#User function Template for python3

class Solution:
    def series(self, n):
        # Code here
        MODULO = 10**9 + 7
        fib = [0, 1]
        while len(fib) < n + 1:
            fib.append((fib[-1] + fib[-2]) % MODULO)
        return fib


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends