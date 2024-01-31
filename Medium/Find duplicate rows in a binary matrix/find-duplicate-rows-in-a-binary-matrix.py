#User function Template for python3

class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        s = set()

        res = []
         
        for i in range(m):
            no = 0
            for j in range(n):
                no += (arr[i][j] << j)
             
            if(no in s):
                res.append(i)
             
            else:
                s.add(no)
         
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        arr = []
        for i in range(n):
            nums = list(map(int, input().strip().split()))
            arr.append(nums)
        ob = Solution()
        ans = ob.repeatedRows(arr, n, m)
        
        for x in ans:
            print(x, end=" ")
            
        print()
        tc -= 1

# } Driver Code Ends