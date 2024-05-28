
from typing import List


class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        # code here
        costs = {w+1: c for w, c in enumerate(cost) if c != -1}
        dp = [float('inf')]*(w+1)
        dp[0] = 0
        
        for total_weight in range(1, w+1):
            for weight, cost in costs.items():
                if total_weight >= weight:
                    dp[total_weight] = min(dp[total_weight], dp[total_weight-weight]+cost)
        return dp[-1] if dp[-1] != float('inf') else -1
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        w = int(input())

        cost = IntArray().Input(n)

        obj = Solution()
        res = obj.minimumCost(n, w, cost)

        print(res)

# } Driver Code Ends