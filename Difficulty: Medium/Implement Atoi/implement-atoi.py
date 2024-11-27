#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        INT_MAX = 2**31 - 1 
        INT_MIN = -2**31 
        
        s = s.strip() 
        if not s: 
            return 0 
        
        sign = 1 
        result = 0 
        index = 0 
        n = len(s) 
        
        if s[index] == '-' or s[index] == '+': 
            sign = -1  if s[index] == '-' else 1 
            index += 1 
        
        while index < n and s[index].isdigit(): 
            digit = int(s[index]) 
            
            if result > (INT_MAX - digit) // 10: 
                return INT_MAX if sign == 1 else INT_MIN 
            
            result = result * 10 + digit 
            index += 1 
        
        return sign * result


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends