class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        dc = {}
        
        res = 0
        
        
        for ind, num in enumerate(arr):
            
            
            if num not in dc:
                
                dc[num] = [ind, -1]
                
                
            else:
                
                dc[num][1] = ind
                
                res = max(res, dc[num][1] - dc[num][0])
                
        return res


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends