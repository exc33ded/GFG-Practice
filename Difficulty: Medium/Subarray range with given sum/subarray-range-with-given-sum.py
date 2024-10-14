#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        dc = {0:1}
        
        cur_sm = 0
        
        res = 0
        
        
        for num in arr:
            
            cur_sm += num
            
            dc[cur_sm] = dc.get(cur_sm, 0) + 1
            
            
            if cur_sm - tar in dc:
                
                
                res += dc[cur_sm - tar]
                
                
        return res

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends