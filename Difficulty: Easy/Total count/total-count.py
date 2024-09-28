#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def totalCount(self, k, arr):
        # code here
        n = len(arr)
        answer = 0 
        for i in range(n):
            answer += arr[i]//k
            if arr[i]%k != 0:
                answer+=1
            else:
                answer+=0
        return answer
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.totalCount(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends