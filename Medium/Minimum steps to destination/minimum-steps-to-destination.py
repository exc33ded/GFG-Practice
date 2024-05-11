#User function Template for python3

class Solution:
    def minSteps(self, D):
        def nd(D):
            return int((-1 + (1 +8*D)**0.5 )/2)
        def check(n):
            tc = []
            maxn = int(n*(n+1)/2)
            for k in range(maxn,-1 , -2):
                tc.append(k)
            return sorted(tc)
        n = nd(D)
        while True:
            #print(n, check(n))
            if D in check(n):
                #print(n)
                break 
            n += 1
        return n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d = int(input())

        ob = Solution()
        print(ob.minSteps(d))

# } Driver Code Ends