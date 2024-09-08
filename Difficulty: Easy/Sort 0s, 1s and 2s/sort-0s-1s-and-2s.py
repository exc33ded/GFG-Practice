class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        freq=[0]*3
        for i in arr:
            freq[i]+=1
        arr[:freq[0]]=[0]*freq[0]
        arr[freq[0]:freq[0]+freq[1]]=[1]*freq[1]
        arr[freq[0]+freq[1]:]=[2]*freq[2]

#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array


if __name__ == "__main__":
    main()

# } Driver Code Ends