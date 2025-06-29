class Solution():
    def can_achieve(self, arr, k, w, target):
        n = len(arr)
        diff = [0] * (n + 1)
        operations = 0
        watered = 0

        for i in range(n):
            watered += diff[i]
            current_height = arr[i] + watered

            if current_height < target:
                needed = target - current_height
                operations += needed
                if operations > k:
                    return False
                watered += needed
                if i + w < n:
                    diff[i + w] -= needed

        return True

    def maxMinHeight(self, arr, k, w):
        low = min(arr)
        high = low + k
        answer = low

        while low <= high:
            mid = (low + high) // 2
            if self.can_achieve(arr, k, w, mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer