class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, arr, N):
        #Code here
        res = []
        leader = arr[N-1]
        res.append(leader)
        for i in range(N-2,-1, -1):
            if leader <= arr[i]:
                leader = arr[i]
                res.append(leader)
                
        return res[::-1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends