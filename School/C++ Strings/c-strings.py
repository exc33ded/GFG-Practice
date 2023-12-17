#User function Template for python3

class Solution:

    def conCat(self,s1,s2):
        # code here
        return s1+s2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s1 = input()
        s2 = input()

        solObj = Solution()

        print(solObj.conCat(s1,s2))
# } Driver Code Ends