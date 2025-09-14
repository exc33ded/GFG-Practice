class Solution:
    def stringStack(self, pat, tar):
        n, m = len(pat), len(tar)
        i, j = n - 1, m - 1  # start from end

        while i >= 0 and j >= 0:
            if pat[i] == tar[j]:
                # match, move both
                i -= 1
                j -= 1
            else:
                # simulate delete: skip two characters in pat
                i -= 2  

        return j < 0
        