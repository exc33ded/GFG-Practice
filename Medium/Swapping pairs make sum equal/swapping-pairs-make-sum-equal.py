class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        s1 = sum(a)
        s2 = sum(b)
        
        ts = s1 + s2
        
        if ts & 1 == 1:
            return -1
        
        mid = ts // 2
        
        d1 = mid - s1
        d2 = mid - s2
        
        sb = set()
        for i in b:
            sb.add(i)
        
        for i in a:
            if i + d1 in sb:
                return 1
        
        return -1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends