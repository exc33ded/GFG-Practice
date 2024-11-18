#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D):
        #Your code here
        N = len(A)
        if D > N:
            D = D%N
        k = A[D:] + A[:D]
        
        for i in range(N):
            A[i] = k[i]





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends