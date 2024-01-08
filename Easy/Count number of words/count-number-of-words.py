#User function Template for python3

class Solution:

    def countWords(self, s):
        # code here
        s = s.replace("\\n", " ")
        s = s.replace("\\t", " ")
        return len(s.split())
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countWords(s))
# } Driver Code Ends