#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        sum = 0
        temp = 1
        for i in range(1,n+1):
            mul = 1
            for j in range(i):
                mul = mul * temp
                temp += 1
            sum = sum+mul
        return sum%1000000007


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends