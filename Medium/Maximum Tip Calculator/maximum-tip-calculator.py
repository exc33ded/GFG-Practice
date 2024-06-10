
from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, a : List[int], b : List[int]) -> int:
        # code here
        higherTip = []
        for i in range(n):
            if a[i] >= b[i]:
                higherTip.append([a[i]-b[i], "a", a[i], b[i]])
            else:
                higherTip.append([b[i]-a[i], "b", a[i], b[i]])
        higherTip.sort(reverse=True)
        
        ans = 0
        for i in range(n):
            if higherTip[i][1] == "a" and x > 0:
                ans += higherTip[i][2]
                x -= 1
            elif higherTip[i][1] == "b" and y > 0:
                ans += higherTip[i][3]
                y -= 1
            elif x > 0:
                ans += higherTip[i][2]
                x -= 1
            else:
                ans += higherTip[i][3]
                y -= 1
            
        
        return ans

 



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

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends