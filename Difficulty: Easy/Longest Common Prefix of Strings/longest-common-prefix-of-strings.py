#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        n = len(arr)
        p=max(arr)
        q=min(arr)
        m=len(q)
        ans=""
        for i in range(m):
            if q[i]==p[i]:
                ans+=q[i]
            else:
                break
        if ans:
            return ans
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends