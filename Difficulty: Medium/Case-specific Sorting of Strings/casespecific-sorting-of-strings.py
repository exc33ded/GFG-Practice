class Solution:
    def caseSort(self,s):
        #code here
        n = len(s)
        upper = []
        lower = []
        for c in s:
            if c.isupper(): upper.append(c)
            if c.islower(): lower.append(c)
        upper.sort()
        lower.sort()
        res = []
        lower_idx = 0
        upper_idx = 0
        for c in s:
            if c.isupper():
                res.append(upper[upper_idx])
                upper_idx += 1
            if c.islower():
                res.append(lower[lower_idx])
                lower_idx += 1
        return "".join(res)
 