
from typing import List


class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        def is_prime(x):
            if x <= 1:
                return False
            if x <= 3:
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True

        a, b = -1, -1
        for i in range(1, (n // 2) + 1):
            if is_prime(i) and is_prime(n - i):
                a = i
                b = n - i
                break

        return [a, b]
        



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

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends