#User function Template for python3
class Solution:
    def firstElement (self, n):
        # code here 
        a = 0 
        b = 1
        for i in range(2,n+1):
            c = (a + b)%1000000007
            a = b 
            b = c
        return b

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends