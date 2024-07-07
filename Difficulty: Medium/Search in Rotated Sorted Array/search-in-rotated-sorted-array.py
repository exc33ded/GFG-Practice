#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        l = 0
        h = len(arr)-1
        while(l<=h):
            mid=l+(h-l)//2
            
            if(A[mid]==key):
                return mid
            
            elif(A[mid]>=A[0]):
                if A[l]<=key and A[mid]>key:
                    h=mid-1
                else:
                    l=mid+1
            
            else:
                if A[mid]<key and A[h]>=key:
                    l=mid+1
                else:
                    h=mid-1
                    
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))

# } Driver Code Ends