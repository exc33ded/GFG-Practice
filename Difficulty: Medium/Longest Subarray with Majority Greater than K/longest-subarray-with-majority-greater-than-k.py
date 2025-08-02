class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        prefix_diffs, diff, max_length = {0: -1}, 0, 0
        for i in range(len(arr)):
            diff += 1 if arr[i] > k else -1
            if diff > 0:
                max_length = i + 1
            elif diff - 1 in prefix_diffs:
                max_length = max(max_length, i - prefix_diffs[diff - 1])
            if diff not in prefix_diffs:
                prefix_diffs[diff] = i
        return max_length
        