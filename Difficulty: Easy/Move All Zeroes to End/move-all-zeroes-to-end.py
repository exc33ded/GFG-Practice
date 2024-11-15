#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	n = len(arr)
    	k = arr.count(0) # Counting the number of zeroes
        lst = list()
        for i in arr:
            if i != 0:
                lst.append(i)
        for k in range(k):
            lst.append(0)
        for i in range(n):
            arr[i] = lst[i]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends