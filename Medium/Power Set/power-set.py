#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
        ans=[]
		def rec(ind,st):
		    if ind==0:
		        ans.append(st)
		        return
		    rec(ind-1,st)
		    st=s[ind-1]+st
		    rec(ind-1,st)
		rec(len(s),"")
		ans.sort()  
		return ans[1:]


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends