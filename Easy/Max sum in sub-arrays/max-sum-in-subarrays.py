#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr, N):
        # Your code goes here
        prev = arr[0]
        curr_sum = 0
        max_sum = float("-inf")
        for i in range(1, N):
            curr_sum = prev + arr[i]
            max_sum = max(max_sum, curr_sum)
            prev = curr_sum - prev
        return max_sum
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.pairWithMaxSum(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends