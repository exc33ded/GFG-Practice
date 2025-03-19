class Solution:
    def maxProfit(self, prices):
        # code here
        _len = len(prices)
        bestFromPos = [0]*(_len+1)
        _max = prices[_len-1]
        for i in range(1,_len):
            _max = max(_max, prices[_len-i-1])        
            bestFromPos[_len-i-1] = max(bestFromPos[_len-i], _max - prices[_len-i-1])        

        minSoFar = prices[0]
        maxProfit = 0
        for i in range(1, _len):
            maxProfit = max(maxProfit, prices[i]-minSoFar + bestFromPos[i+1])            
            minSoFar = min(minSoFar, prices[i])            

        return maxProfit



#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends