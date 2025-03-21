class Solution:  
    def findMaxSum(self,arr):
        # code here
        stolen, notstolen, n = 0, 0, len(arr)
        for i in range(n):
            n_stolen = max(stolen, notstolen+arr[i]) 
            n_notstolen = max(stolen, notstolen)
            stolen, notstolen = n_stolen, n_notstolen
        return max(stolen, notstolen)

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends