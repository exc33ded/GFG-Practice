#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #code here
        new = -1
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i,count in freq.items():
            if count > (len(arr)/2):
                new = i
            
        return new

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
from sys import stdin


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(arr))
        print("~")
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends