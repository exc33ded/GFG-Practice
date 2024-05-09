#User function Template for python3

class Solution:
    def solve(self, indx, a, k, n, v, ans):
        if k == 0:
            ans.append(v[:])
            return

        if indx == n or k < 0:
            return

        for i in range(indx, n):
            if i != indx and a[i] == a[i - 1]:
                continue
            v.append(a[i])
            self.solve(i + 1, a, k - a[i], n, v, ans)
            v.pop()

    def CombinationSum2(self, arr, n, k):
        arr.sort()
        v = []
        ans = []
        self.solve(0, arr, k, len(arr), v, ans)

        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ob = Solution()
    result = ob.CombinationSum2(arr, n, k)
    for row in result:
        print(*row)
    if not result:
        print()

# } Driver Code Ends