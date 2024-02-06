#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
		res = ""
		
		for char in S:
		    if char not in res:
		        res += char
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends