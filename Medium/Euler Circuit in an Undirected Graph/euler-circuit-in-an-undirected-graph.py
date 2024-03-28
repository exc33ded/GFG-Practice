#User function Template for python3

class Solution:
	def isEularCircuitExist(self, n, x):
		#Code here
        return int(all(not len(i)&1 for i in x))

#{ 
 # Driver Code Starts
#Initial Template for python3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEularCircuitExist(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends