#User function Template for python3

class Solution:
    def reverseWords(self, s):
        # code here
        a = s[::-1]  # reverse the entire string
        b = a.split(".")[::-1] # every element is reversed and splitted 
        return ".".join(b) # rejoined after splittion 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends