#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import math

class Solution:
    def smallestNumber (self, S, D):
        # code here 
        def calculatePower(x, n):
            ans = math.exp(math.log(x) * n) #O(1)
            ans = round(ans)
            return ans
                
        def smallest_number(digit):
            if digit == 1:
                return 1
            return calculatePower(10,digit-1)
            
        def add_nines(digit):
            if digit == 0:
                return 0
            return calculatePower(10,digit)-1
        
        def end_digits(nines,reminder):
            total = 0
            if reminder != 0:
                total += smallest_number(nines+1)
                total *= reminder
                
            total += add_nines(nines)
            return total
                
                
        nines = S//9
        reminder = S % 9
        
        is_rem = 0
        if reminder > 0:
            is_rem = 1
            
        if (nines + is_rem) > D:
            return -1
        elif (nines + is_rem ) == D:
            return (end_digits(nines,reminder))
        else:
            S1 = S-1
            nines = S1//9
            reminder = S1 % 9
            return (smallest_number(D) + end_digits(nines,reminder))




#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends