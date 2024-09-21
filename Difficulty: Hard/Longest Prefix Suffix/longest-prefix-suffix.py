#User function Template for python3

class Solution:
	def lps(self, str):
		# code here
        pst = [0 for _ in range(len(s))]
    	j = 0
    	for i in range(1, len(s)):
    		while j > 0 and s[j] != s[i]:
    			j = pst[j - 1]
    
    		if s[i] == s[j]:
    			j += 1
    			pst[i] = j
    
    	return pst[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.lps(s)
        print(answer)

# } Driver Code Ends