#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       
       start = 0
       end = 0
       sum = 0
       
       if s == 0:
           return [-1]
       
       while end != n:
           
           sum = sum + arr[end]
           
           # If sumcurrent sum gets greater than the given sum
           while sum > s:
               sum = sum - arr[start]
               start += 1
           
           
           # If current sum equals the given sum
           if sum == s:
               return [start + 1, end + 1]
                    
           end += 1

       return [-1]
           
       



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