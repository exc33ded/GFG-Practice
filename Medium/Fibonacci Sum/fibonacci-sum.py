#User function Template for python3

class Solution:
    def fibSum (self,N):
        #code here
        num  =[0,1]
        if N < 2:
            return sum(num)
            
        for i in range(2,N + 1):
            num.append((num[-1] % 1000000007)+(num[-2] % 1000000007))
        return sum(num) % 1000000007

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.fibSum(N))
# } Driver Code Ends