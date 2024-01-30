#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        def isOperator(x):
            if x == "+":
                return True
         
            if x == "-":
                return True
         
            if x == "/":
                return True
         
            if x == "*":
                return True
         
            return False
                
        s = []
 
        # length of expression
        length = len(post_exp)
     
        # reading from right to left
        for i in range(length):
     
            # check if symbol is operator
            if (isOperator(post_exp[i])):
     
                # pop two operands from stack
                op1 = s[-1]
                s.pop()
                op2 = s[-1]
                s.pop()
     
                # concat the operands and operator
                temp = post_exp[i] + op2 + op1
     
                # Push string temp back to stack
                s.append(temp)
     
            # if symbol is an operand
            else:
     
                # push the operand to the stack
                s.append(post_exp[i])
     
        
        ans = ""
        for i in s:
            ans += i
        return ans
        
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        postfix = input()
        ob = Solution()
        res = ob.postToPre(postfix)
        print(res)
# } Driver Code Ends