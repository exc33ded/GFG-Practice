#User function Template for python3
class Solution:
    def findMin(self, arr):
        #complete the function here
        low=0
        high=len(arr)-1
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            if arr[low]<arr[high]:
                ans=min(ans,arr[low])
                break
            if arr[mid]>=arr[low]:
                ans=min(ans, arr[low])
                low=mid+1
            else:
                ans=min(ans, arr[mid])
                high=mid-1
                
        return ans 


#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends