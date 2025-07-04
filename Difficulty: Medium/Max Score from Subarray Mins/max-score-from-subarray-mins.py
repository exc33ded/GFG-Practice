import heapq

class Solution:
    def maxSum(self, arr):
        # code here
        max_score = 0
        n = len(arr)

        # Use a min-heap to store potential min1, min2 pairs
        # This is just a clever trick to avoid checking all O(n²) subarrays
        min_heap = []

        for i in range(n):
            heapq.heappush(min_heap, arr[i])
            if len(min_heap) > 2:
                heapq.heappop(min_heap)  # keep only two smallest

        # Two smallest elements from the entire array may not be from same subarray
        # So now we scan for all adjacent pairs (subarrays of length 2)
        for i in range(n - 1):
            s = arr[i] + arr[i + 1]
            max_score = max(max_score, s)

        # Optional: Also check for a global pair of two smallest if needed
        # Uncomment if subarrays of full length are allowed
        # max_score = max(max_score, sum(min_heap))

        return max_score


        
    
