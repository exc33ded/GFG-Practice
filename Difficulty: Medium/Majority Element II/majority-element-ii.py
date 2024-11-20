class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        arr.sort()
        n = len(arr)//3
        count = 1
        ans = []
        
        if len(arr)> 1 and arr[0] == arr[1]:
            count = 2
        else:
            count = 1
            
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                count += 1
            else:
                if count > n:
                    ans.append(arr[i-1])
                count = 1
                
        if count > n:
            ans.append(arr[-1])
            
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends