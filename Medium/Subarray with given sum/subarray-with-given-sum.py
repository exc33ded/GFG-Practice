#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        Sum=arr[0]
        res=[]
        start=0
        end=1
        
        while end<=n:
            
            while Sum>s and start<end-1:
                Sum-=arr[start]
                start+=1
            
            if Sum==s:
                res.append(start+1)
                res.append(end)
                return res
                
            if end<n:
                Sum+=arr[end]
            end+=1
                
        res.append(-1)    
        return res





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends