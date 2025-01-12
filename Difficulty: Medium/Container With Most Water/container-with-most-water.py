
class Solution:
    def maxWater(self, A):
        # code here
        le = len(A)
        low,hi,maxArea = 0,le-1,0
        while(low<hi):
            currArea = min(A[low],A[hi])*(hi-low)
            maxArea = max(maxArea,currArea)
            if(A[low]>A[hi]):
                hi-=1
            else:
                low+=1
        return maxArea


#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends