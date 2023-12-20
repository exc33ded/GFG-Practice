#User function Template for python3

class Solution:
    def orderString(self, s, n):
        # code 
        s.sort()
        return s[0], s[n-1]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n= int(input())
        s = input().split()
        ob = Solution()
        ans = ob.orderString(s,n)
        print(ans[0], ans[1])
        
# } Driver Code Ends