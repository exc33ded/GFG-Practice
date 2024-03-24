#User function Template for python3
class Solution:
	def NBitBinary(self, N):
		# code here
        def _NBitBinary(N):
            if N== 1:
                return [['1', 1]]
            last = _NBitBinary(N-1)
            new = []
            for l in last:
                if l[1] == 0:
                    l[0] += '1'
                    l[1] = 1
                else:
                    new.append([l[0]+'1', l[1]+1])
                    l[0] += '0'
                    l[1] -= 1
                    
            return (last + new)
        last = _NBitBinary(N)
        ans = [l[0] for l in last]
        return sorted(ans, reverse=True)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends