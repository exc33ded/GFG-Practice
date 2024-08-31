#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        m = len(arr1)
        n = len(arr2)
        sum1=0
        sum2=0
        i1=0
        i2=0
        res=0
        
        while i1<m and i2<n:
            if arr1[i1]<arr2[i2]:
                sum1=sum1+arr1[i1]
                i1=i1+1
            elif arr1[i1]>arr2[i2]:
                sum2=sum2+arr2[i2]
                i2=i2+1
            else:
                res=res+max(sum1,sum2)+arr1[i1]
                sum1=0
                i1=i1+1
                sum2=0
                i2=i2+1
        
        if i1==m:
            sum2=sum2+sum(arr2[i2:])
        else:
            sum1=sum1+sum(arr1[i1:])
            
        res=res+max(sum1,sum2)
                
        return res


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends