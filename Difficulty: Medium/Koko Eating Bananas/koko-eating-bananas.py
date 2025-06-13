#User function Template for python3

class Solution:
    def eatBananas(self, arr, s):
        cnt = 0
        for i in arr:
            cnt += (i + s - 1) // s
        return cnt

    def kokoEat(self,arr,k):
        low, high = 1, max(arr)
        while low <= high:
            mid = (low + high) // 2
            hours = self.eatBananas(arr, mid)
            if hours > k:
                low = mid + 1
            else:
                high = mid - 1
        return low