#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		# code here
		a = int(s1, 2)
		b = int(s2, 2)
		
		s = a + b
		
		return bin(s)[2:]