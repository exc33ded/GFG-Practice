class Solution:
    def validgroup(self, arr, k):
        from collections import Counter
        if k == 1:
            return True
        if len(arr) % k:
            return False
        freqs = sorted(map(list, Counter(arr).items()))
        n = len(freqs)
        group_start_i = 0
        while group_start_i < n:
            if group_start_i + k > n:
                return False
            group_freq = freqs[group_start_i][1]
            freqs[group_start_i][1] = 0
            next_group_start_i = group_start_i + 1
            for i in range(group_start_i + 1, group_start_i + k):
                freqs[i][1] -= group_freq
                if (freqs[i][1] < 0
                    or freqs[i][1] == 0 and freqs[i - 1][1] > 0
                    or freqs[i - 1][0] + 1 != freqs[i][0]
                ):
                    return False
                if freqs[i][1] == 0:
                    next_group_start_i = i + 1
            group_start_i = next_group_start_i
        return True