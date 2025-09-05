class Solution:
    def maxSum(self, a): 
        # Code here
        n = len(a)
        sum1 = 0
        ans = 0
        res = 0
        for i in range(n):
            sum1 += a[i]
            res += a[i]*i
        ans = max(ans,res)
        for i in range(n):
            res = res + a[i]*n - sum1
            ans =max(ans,res)
        return ans
    
            