#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        a = [0] * n
        j = 0
        k = 0

        for i in range(n):
            if arr[i] < 0:
                a[j] = arr[i]
                j += 1
            else:
                arr[k] = arr[i]
                k += 1

        p = 0
        for i in range(k, n):
            arr[i] = a[p]
            p += 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends