#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        neg = False
        if s[0] == "-":
            neg = True
            s = s[1:]
            
        if not s.isdigit():
            return -1
        
        res = int(s)
        return -res if neg else res
        

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends