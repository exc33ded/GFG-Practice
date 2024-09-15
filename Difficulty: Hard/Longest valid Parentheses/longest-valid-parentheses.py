# User function Template for Python3

class Solution:
    def maxLength(self, s):
        # code here
        op=0
        n=len(s)
        cl=0
        ans=0
        for i in range(n):
            if s[i]=="(":
                op+=1
            else:
               cl+=1
            if op==cl:
                ans=max(ans,op+cl)
            elif cl>op:
                op=0
                cl=0
        op=0
        cl=0
        for i in range(n-1,-1,-1):
            if s[i]=="(":
                op+=1
            else:
               cl+=1
            if op==cl:
                ans=max(ans,op+cl)
            elif cl<op:
                op=0
                cl=0
        return ans 


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))

# } Driver Code Ends