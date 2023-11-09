#User function Template for python3

class Solution:
    def columnWithMaxZeros(self,arr,N):
        
        res=-1
        max_zeros=0
        
        for j in range(N):
            col_sum=0
            for i in range(N):
                col_sum=col_sum+arr[i][j]
            if N-col_sum>max_zeros:
                max_zeros=N-col_sum
                res=j
        
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


# } Driver Code Ends