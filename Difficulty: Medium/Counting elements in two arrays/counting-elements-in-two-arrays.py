class Solution:
    def countLessEq(self, a, b):
        # code here
        b.sort()
        result = []
        def binary_search(b, target):
            low, high = 0, len(b) - 1
            while low <= high:
                mid = (low + high) // 2
                if b[mid] <= target:
                    low = mid + 1 
                else:
                    high = mid - 1
            return low
        for x in a:
            count = binary_search(b, x)
            result.append(count)
        
        return result