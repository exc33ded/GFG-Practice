#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
		# code here
		max_num = arr[0]
        for i in arr:
            if max_num < i:
                max_num = i
        return max_num

#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends