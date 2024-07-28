#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr):
		# code here
		row = len(arr)
	    col = len(arr[0])
	    prevjS = col+1
	    prevR = -1
	    for i in range(row):
	        left = 0
	        right = col-1
	        prevj = -1
	        while left<=right:
	            mid = left+(right-left)//2
	            if arr[i][mid]==0:
	                left = mid+1
	            elif arr[i][mid]==1:
	                prevj=mid
	                right = mid-1
	           
	        if prevj !=-1:
	            if prevjS>prevj:
	                prevjS=prevj
	                prevR = i
	        
	    return prevR


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends