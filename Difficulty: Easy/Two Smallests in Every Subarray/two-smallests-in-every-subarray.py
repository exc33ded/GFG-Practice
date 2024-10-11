class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        if len(arr) < 2:
            return -1
        ma = 0
        f = 0
        for i in arr:
            ma = max(ma, (f+i))
            f = i
        return ma


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends