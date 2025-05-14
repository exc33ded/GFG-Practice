class Solution:
	def countSubstring(self, s):
		# code here
        freq={}
	    for i in s:
	        freq[i]=freq.get(i,0)+1
	    ans=0
	    for i in freq.values():
	        ans+=(i*(i+1))//2
	    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.countSubstring(s)

        print(answer)
        print("~")

# } Driver Code Ends