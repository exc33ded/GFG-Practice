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
