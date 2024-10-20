#User function Template for python3
class Solution:
	def countgroup(self,a): 
		#Complete the function
		n = len(a)
		ans = 0
        mod = 1e9 +7
        for i in range(n):
            ans^=a[i]
        val =1
        for i in range(n-1):
            val*=2
            val%=mod
        return int(val-1) if (ans ==0)  else 0



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends