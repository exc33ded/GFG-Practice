#User function Template for python3

class Solution:
    def check(self,num):
        if (num)%8==0:
            return 1
        else:
            return -1
               
    def DivisibleByEight(self,S):
       #code here
        if len(S)<4:
            return self.check(int(S))
        else:
            num = S[len(S)-3:]
            return self.check(int(num))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends