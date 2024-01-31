#User function Template for python3

class Solution:
    def factorial(self, N):
        #code here
        def fact(N):
            if N <= 1:
                return 1
            else:
                return N * fact(N-1)
        return str(fact(N))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Endshttps://media.geeksforgeeks.org/img-practice/prod/courses/5/Web/Content/Clock-4_1706701529.gif