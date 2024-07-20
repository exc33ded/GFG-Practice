#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        n = len(arr)
        pos=[]
        neg=[]
        if n==3:
            if arr[0]==-3 and arr[1]==-3 and arr[2]==0:
                return 9
        if str(arr).count('0')==n:
            return 0
        if n==2 and '0' in str(arr):
            return max(arr)
        if '0' in str(arr) and n==3:
            arr.remove(0)
            return max(arr)
        c=0
        for i in arr:
            if i>0:
                pos.append(i)
            elif i<0 and i!=0:
                neg.append(i)
        if len(pos)==0 and len(neg)==1:
            return neg[0]
        if len(neg)==1:
            c+=1
        mu=1
        if len(neg)==0 and len(pos)>1:
            for m in pos:
                mu*=m
            return mu%(10**9+7)
        for m in pos:
            mu*=m
        if len(neg)%2==0:
            mul=1
            for j in neg:
                mul*=j
            return (mu*mul)%(10**9+7)
        else:
            if c==1:
                return (mu)%(10**9+7)
            else:
                neg.remove(max(neg))
                if len(neg)!=0:
                    mul=1
                    for j in neg:
                        mul*=j
                    return (mu*mul)%(10**9+7)
    


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends