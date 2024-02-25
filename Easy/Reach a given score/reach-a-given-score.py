#User function Template for python3
class Solution:
    def count(self, n: int) -> int:
        #your code here
        ways = [0] * (n + 1)
   
        ways[0] = 1

        moves = [3, 5, 10]
        for i in range(3):
            for j in range(moves[i], n+1):
                ways[j] += ways[j - moves[i]]
       
        return ways[n]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ob = Solution()
        print(ob.count(n))
        
# } Driver Code Ends