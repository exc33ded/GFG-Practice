#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        # Code here
        N = len(intervals)
        if N==1: return 0

        count = 0
        intervals.sort(key = lambda i:i[1])
        res = intervals[0][1]
        
        for s, t in intervals[1:]:
            if s>=res: res=t
            else:count+=1
        
        return count

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends