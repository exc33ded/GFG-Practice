#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        l = list(map(int, str(n)))

        #Initialize a variable to store the sum of cubes of digits
        s = 0

        #Loop through each digit in the number
        for i in l:
            #Add the cube of each digit to the sum
            s += i**3

        #Check if the sum of cubes is equal to the original number
        if n == s:
            return "true"
        else:
            return "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends