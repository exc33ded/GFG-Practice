#User function Template for python3
from itertools import zip_longest

from collections import deque
class Solution:
	def addBinary(self, A, B):
		# code here
		
		res = deque()
		
		rem = 0
		
		A = A.lstrip("0")
		
		B = B.lstrip("0")
		
		for sym1, sym2 in zip_longest(A[::-1], B[::-1], fillvalue="0"):
		    
		    num1 = int(sym1)
		    
		    num2 = int(sym2)
		    
		    
		    if num1 + num2 + rem == 3:
		        
		        res.appendleft("1")
		        
		        rem = 1
		        
		    elif num1 + num2 + rem == 2:
		        
		        
		        
		        res.appendleft("0")
		        
		        rem = 1
		        
		    elif num1 + num2 + rem == 1:
		        
		        
		        
		        res.appendleft("1")
		        
		        rem = 0
		        
		    else:
		        
		        
		        res.appendleft("0")
		        
		        rem = 0
		        
		       
		        
		        
		if rem:
		     
		      res.appendleft("1")
		     
	
		     
		     
		return "".join(res) if res else "0"
		        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends