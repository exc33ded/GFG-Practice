#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        ln = len(arr)
        l = 0
        m = 0
        while m < ln:
            if arr[m] != 0:
                if m != ln-1 and arr[m] == arr[m+1]:
                    arr[m]*=2
                    arr[m], arr[l] = arr[l], arr[m]
                    l+=1
                    arr[m+1] = 0
                else:
                    arr[m], arr[l] = arr[l], arr[m]
                    l+=1  
            m+=1
        return arr

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        t -= 1


# } Driver Code Ends