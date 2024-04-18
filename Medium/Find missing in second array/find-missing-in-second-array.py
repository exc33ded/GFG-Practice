#User function Template for python3


class Solution:
    def findMissing(self,A, B, N,M):
    # code here
        new=set(B)
        lists=[]
        for i in A:
            if i not in new:
                lists.append(i)
        return lists



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
   # n=int(input())
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ob=Solution()
    ans=ob.findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
# } Driver Code Ends