#User function Template for python3

def max_sum(a,n):
    #code here
    sum1 = 0
    ans = 0
    res = 0
    for i in range(n):
        sum1 += a[i]
        res += a[i]*i
    ans = max(ans,res)
    for i in range(n):
        res = res + a[i]*n - sum1
        ans =max(ans,res)
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends