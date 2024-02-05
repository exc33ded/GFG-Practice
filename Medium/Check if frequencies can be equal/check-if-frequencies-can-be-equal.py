#User function Template for python3
class Solution:
    def sameFreq(self, s):
        # code here
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        values = list(d.values())
        freq_set = set(values)
        
        if len(freq_set) == 1:
            return True
        
        if len(freq_set) == 2:
            min_freq, max_freq = min(freq_set), max(freq_set)
            min_freq_count = values.count(min_freq)
            max_freq_count = values.count(max_freq)
            
            if (min_freq_count == 1 and min_freq == 1) or (max_freq_count == 1 and max_freq - min_freq == 1):
                return True
        
        
        
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