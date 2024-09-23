#User function Template for python3


from collections import defaultdict

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        countT, window = defaultdict(int), defaultdict(int)  # using defaultdict for fast lookup
        
        for c in p:
            countT[c] += 1  # initialize count for string p characters

        have, need = 0, len(countT)
        res, reslen = [-1, -1], float("infinity")  
        l = 0  # sliding window start here
        
        for r in range(len(s)):    
            c = s[r]
            window[c] += 1  # add current character to window

            if c in countT and window[c] == countT[c]:
                have += 1  # increment 'have' only when counts match

            while have == need:   # if both are equal, update result and length
                # update result
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = (r - l + 1)   
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1  # decrement 'have' only when condition is met
                l += 1
        
        l, r = res
        return s[l:r+1] if reslen != float("infinity") else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends