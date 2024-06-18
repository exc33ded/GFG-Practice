#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        #code here
        count = 0
        max_side = 2 * r
        
        for a in range(1, max_side + 1):
            for b in range(1, max_side + 1):
                if a * a + b * b <= 4 * r * r:
                    count = count + 1
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends