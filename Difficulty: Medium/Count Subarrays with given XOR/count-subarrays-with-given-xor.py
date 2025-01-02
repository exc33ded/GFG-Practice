class Solution:
    def subarrayXor(self, arr, m):
        # code here
        xor_acc = 0
        xor_rem_count = {0: 1}
        ans = 0
        for i in arr:
            xor_acc = xor_acc ^ i
            if xor_rem_count.get(xor_acc ^ m, None) is not None:
                ans += xor_rem_count.get(xor_acc ^ m, 0)
            xor_rem_count[xor_acc] = xor_rem_count.get(xor_acc, 0) + 1
        return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends