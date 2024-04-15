#User function Template for python3
import bisect as bi
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        n = len(a)
        max = -1

        for i in range(0, n):
            if (a[i] > max):
                max = a[i]

        max2 = max

        for i in range(0, n):
            if (b[i] > max2):
                max2 = b[i]

        h = [0] * (max2 + 1)
        for i in range(0, n):
            h[b[i]] += 1

        for i in range(1, max + 1):
            h[i] += h[i - 1]

        ans = []
    
        for i in range(0, q):
            ans.append(h[a[query[i]]])

        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends