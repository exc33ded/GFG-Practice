#User function Template for python3
class Solution:
    def swapNibbles (self, N):
        # code here 
        a= N>>4&((1<< 4) - 1)

        b= (N&((1<< 4) - 1))<<4

        return a+b


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends