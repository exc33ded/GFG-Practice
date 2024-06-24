#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
        mid = n + 1
        if  q in range(2, 2*n+1):
            if q == mid  :
                return n
            elif q < mid :
                return (q-1 )
            else:  
                return (2*n - q +1 )
        else : return 0 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends