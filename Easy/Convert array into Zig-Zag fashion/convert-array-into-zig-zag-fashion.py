
from typing import List


class Solution:
    def zigZag(self, n : int, arr : List[int]) -> None:
        # code here
        ptr=0
        mov=1
        while(ptr<n and mov<n):
            if mov%2!=0 and arr[ptr]<arr[mov]:
                mov+=1
                ptr+=1
            elif mov%2!=0 and arr[ptr]>arr[mov]:
                arr[ptr]=arr[mov]+arr[ptr]
                arr[mov]=arr[ptr]-arr[mov]
                arr[ptr]=arr[ptr]-arr[mov]
            elif mov%2==0 and arr[ptr]>arr[mov]:
                mov+=1
                ptr+=1
            elif mov%2==0 and arr[ptr]<arr[mov]:
                arr[ptr]=arr[mov]+arr[ptr]
                arr[mov]=arr[ptr]-arr[mov]
                arr[ptr]=arr[ptr]-arr[mov]
        



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

    def isZigzag(n: int, arr: List[int]) -> bool:
        f = 1

        for i in range(1, n):
            if f:
                if arr[i - 1] > arr[i]:
                    return False
            else:
                if arr[i - 1] < arr[i]:
                    return False
            f = f ^ 1

        return True

    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        obj.zigZag(n, arr)
        check = True
        check = isZigzag(n, arr)
        if check:
            print("1")
        else:
            print("0")

# } Driver Code Ends