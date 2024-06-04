#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        start, end = 0, n - 1
        while(start<end):
            mid = (start+end)//2
            if arr[mid] > arr[end]:
                start = mid + 1
            else:
                end = mid
                
        return start
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends