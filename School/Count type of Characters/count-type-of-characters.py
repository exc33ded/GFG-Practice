#User function Template for python3

class Solution:
    def count (self,s):
        # your code here
        lower = 0
        upper = 0
        num = 0
        sp = 0
        for i in s:
            if i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            elif i.isnumeric():
                num += 1
            else:
                sp += 1
            
        return [upper, lower, num, sp]
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
# Contributed By: Pranay Bansal

# } Driver Code Ends