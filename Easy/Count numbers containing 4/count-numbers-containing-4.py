
class Solution:
    def countNumberswith4(self, N : int) -> int:
        # code here
        count=0
        arr=[x for x in range(1,N+1)]
        for num in arr:
            str1=str(num)
            if "4" in str1:
                count+=1
        return count



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends