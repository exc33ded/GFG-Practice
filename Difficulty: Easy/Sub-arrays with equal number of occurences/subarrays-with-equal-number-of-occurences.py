#User function Template for python3
from collections import defaultdict
class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        dc = defaultdict(int)
        dc[0] = 1
        sm = 0
        res = 0
        
        for num in arr:
            if num ==x:
                sm+=1
            elif num == y:
                sm-=1
            res += dc[sm]
            dc[sm]+=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends