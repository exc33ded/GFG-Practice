#User function Template for python3

class Solution:
    def check (self,s):
        # your code here
        a = set(s)
        if len(a) == 1:
            return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    if ob.check (s):
        print ("YES")
    else:
        print ("NO")
        
# Contributed By: Pranay Bansal

# } Driver Code Ends