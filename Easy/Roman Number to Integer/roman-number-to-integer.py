#User function Template for python3

class Solution:
    def romanToDecimal(self, s): 
        # code here
        roman = {
            "I": 1,
            "V" :5,
            "X" :10,    
            "L" :50,
            "C" :100,   
            "D" :500,   
            "M" :1000
        }
        
        res = 0
        
        for x, y in zip(s, s[1:]):
            if roman[x] < roman[y]:
                res -= roman[x]
            else:
                res += roman[x]
                
        return res + roman[s[-1]]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends