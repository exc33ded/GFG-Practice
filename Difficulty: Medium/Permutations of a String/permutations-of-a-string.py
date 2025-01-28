#User function Template for python3
from itertools import *
class Solution:
    def findPermutation(self, S):
        # Code here
        arr = permutations(S)
        lst = []
        for i in arr:
            i = "".join(i)
            lst.append(i)
        lst = list(set(lst))
        return lst



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends