#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        pos=[i for i in arr if i>=0]
        neg=[i for i in arr if i<0]
        arr[:]=pos[:]
        index=1
        for i in neg:
            arr.insert(index,i)
            index+=2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends