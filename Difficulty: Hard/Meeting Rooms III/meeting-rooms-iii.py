#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq


# } Driver Code Ends

#User function Template for python3
class Solution:
    def mostBooked(self, n, meetings):
        #code here
        from heapq import heapify, heappop, heappush, heapreplace
        in_use_rooms = []
        free_rooms = list(range(n))
        heapify(free_rooms)
        meetings.sort()
        counts = [0] * n
        for start, end in meetings:
            while in_use_rooms and in_use_rooms[0][0] <= start:
                _, freed_room = heappop(in_use_rooms)
                heappush(free_rooms, freed_room)
            if free_rooms:
                room = heappop(free_rooms)
                heappush(in_use_rooms, (end, room))
            else:
                old_end, room = in_use_rooms[0]
                delay = old_end - start
                heapreplace(in_use_rooms, (end + delay, room))
            counts[room] += 1
        max_room, _ = max(enumerate(counts), key=lambda x: (x[1], -x[0]))
        return max_room


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().split()
    it = iter(input)
    t = int(next(it))
    while t > 0:
        t -= 1
        n = int(next(it))
        m = int(next(it))
        meetings = []
        for _ in range(m):
            s = int(next(it))
            e = int(next(it))
            meetings.append([s, e])
        sol = Solution()
        res = sol.mostBooked(n, meetings)
        print(res)
        print("~")
# } Driver Code Ends