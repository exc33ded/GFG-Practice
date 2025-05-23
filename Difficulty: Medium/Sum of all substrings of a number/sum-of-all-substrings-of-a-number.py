class Solution:
    def sumSubstrings(self,s):
        # code here
        res = cur = int(s[0])
        for i in range(1, len(s)):
            cur = cur * 10 + int(s[i]) * (i + 1)
            res += cur
        return res