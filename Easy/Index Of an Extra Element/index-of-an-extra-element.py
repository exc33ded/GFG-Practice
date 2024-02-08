class Solution:
    def findExtra(self,a,b,n):
        #add code here
        start = 0
        end = n - 1
        
        while (start < end):
            mid = start + (end - start)//2
            
            if a[mid] == b[mid]:
                start = mid + 1
            else:
                end = mid
                
        return start

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
# } Driver Code Ends