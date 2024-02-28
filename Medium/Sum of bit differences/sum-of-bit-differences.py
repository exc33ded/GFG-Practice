#User function Template for python3
class Solution:

	
	def sumBitDifferences(self,arr, n):
    	# code here
        ans=0
    	for i in range(32):
    	    o=0;z=0
    	    for j in arr:
    	        if j&(1<<i):
    	            o+=1
    	        else:
    	            z+=1
    	    ans+=(o*z)
    	return 2*ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends