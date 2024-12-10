class Solution:
    def mergeArrays(self, arr1, arr2):
        # code here
        n = len(arr1)
        m = len(arr2)
        i=len(arr1)-1
        j=0
        while i>=0 and j<len(arr2) and arr1[i]>arr2[j]:
            arr1[i],arr2[j]=arr2[j],arr1[i]
            i-=1
            j+=1
        
        # resort
        arr1.sort()
        arr2.sort()
        return arr1,arr2


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends