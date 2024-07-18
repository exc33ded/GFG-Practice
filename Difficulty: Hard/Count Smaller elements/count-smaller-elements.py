from sortedcontainers import SortedList
class Solution:
	def constructLowerArray(self,arr):
        n = len(arr)
	    S = SortedList()
	    res  = [0]*n
	    for i in range(len(arr)-1,-1,-1):
	        res[i] = S.bisect_left(arr[i])
	        S.add(arr[i])
	    return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.constructLowerArray(arr)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends