#User function Template for python3


class Solution:
    def compareFrac (self, str):
        f1,f2=str.split(', ')
        v1,v2=eval(f1),eval(f2)

        if v1==v2:
            return 'equal'
        elif v1<v2:
            return f2
        else:
            return f1




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends