#User function Template for python3
from collections import Counter

class Solution:
    def sameFreq(self, s):
        # code here
        count=Counter(s)
        
        freq=Counter(count.values())
        
        if len(freq) >= 3:
            return False
            
        if len(freq) == 1:
            return True
            
        mn,mx = min(count.values()), max(count.values())
        
        if freq[mx] == 1 and mn+1 == mx:
            return True
            
        if 1 in freq and freq[1] == 1:
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends