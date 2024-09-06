#User function Template for python3

def base9(n):
    """ Convert a number to base-9 representation """
    result = 0
    multiplier = 1
    while n > 0:
        result += (n % 9) * multiplier
        n //= 9
        multiplier *= 10
    return result

class Solution:

    def findNth(self, N):
        # Base-9 conversion to skip numbers containing '9'
        return base9(N)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends