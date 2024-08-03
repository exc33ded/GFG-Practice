#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meetings = [(start[i], end[i]) for i in range(len(start))]
        meetings.sort(key = lambda x:x[1])
        
        ans = 1
        time_limit = meetings[0][1]
        
        for i in range(1,len(start)):
            if meetings[i][0] > time_limit:
                ans += 1
                time_limit = meetings[i][1]
                
        return ans

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends