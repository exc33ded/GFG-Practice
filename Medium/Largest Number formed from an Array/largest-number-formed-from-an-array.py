#User function Template for python3
from functools import cmp_to_key
class Solution:

	def printLargest(self, n, arr):
	    # code here
	    
	    def  compare(n1, n2):
	        if n1 + n2 >  n2 + n1:
	            return -1
	        return 1
	    arr = sorted(arr, key = cmp_to_key(compare))
        return str(int("".join(arr)))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

# } Driver Code Ends