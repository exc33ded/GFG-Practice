#User function Template for python3
class Solution:
	def count(self,arr, n, x):
		# code here
		def floor(arr, n, x):
		    start = 0
		    end = n - 1
		    res = -1
		    while(start <= end):
		        mid = start + (end - start)//2
		        if arr[mid] == x:
		            res = mid
		            start = mid + 1
		        elif arr[mid] > x:
		            end = mid - 1
                else:
                    start = mid + 1
            return res
            
        def ceil(arr, n, x):
		    start = 0
		    end = n - 1
		    res = -1
		    while(start <= end):
		        mid = start + (end - start)//2
		        if arr[mid] == x:
		            res = mid
		            end = mid - 1
		        elif arr[mid] > x:
		            end = mid - 1
                else:
                    start = mid + 1
            return res
            
        low = floor(arr, n, x)
        high = ceil(arr, n, x)

        if low == -1:
            return 0
        else:
            return abs(high - low - 1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends