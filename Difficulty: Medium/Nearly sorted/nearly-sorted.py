class Solution:
    def nearlySorted(self, arr, k):  
        #code here
        import heapq
        hp=[]
        for ix,ve in enumerate(arr):
            heapq.heappush(hp,ve)
            if ix>=k:
                arr[ix-k]=heapq.heappop(hp)
        for ix in range(k):
            arr[-k+ix]=heapq.heappop(hp)