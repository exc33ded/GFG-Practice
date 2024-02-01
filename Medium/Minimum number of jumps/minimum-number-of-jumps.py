#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
        mx = 0
        curr = 0
        count = 0
        
        for i in  range(n-1):
            mx = max(mx, arr[i]+i)
            if (i == curr):
                count += 1
                curr = mx
        if curr >= n-1:
            return count 
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends