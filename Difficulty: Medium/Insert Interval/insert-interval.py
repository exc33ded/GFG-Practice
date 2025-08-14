class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        n=len(intervals)
        flag=True
        for i in range(n):
            if(intervals[i][0]>newInterval[0]):
                intervals.insert(i,newInterval)
                flag=False
                break
        if flag:intervals.append(newInterval)
        prev=intervals[0]
        res=[]
        for i in range(n+1):
            inv=intervals[i]
            if(prev[1]>=inv[0]):
                if(prev[1]<inv[1]):
                    # overlapping
                    prev[1]=inv[1]    
            else:
                if(prev[0]!=-1):
                    res.append(prev)
                prev=inv
        res.append(prev)
        return res