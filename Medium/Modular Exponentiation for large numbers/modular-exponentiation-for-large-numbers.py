#User function Template for python3

class Solution:
	def PowMod(self, x, n, m):
		# Code here
		if n==1:
		    return x%m
		if n%2==0:
		    t=self.PowMod(x, n/2,m)
		    return (t*t)%m
        else:
            t = self.PowMod(x, n//2, m)
            return (t*t*x)%m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends