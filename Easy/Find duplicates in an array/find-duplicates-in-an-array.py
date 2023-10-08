class Solution:
    def duplicates(self, arr, n):
        
        frequency = {}
        result =[]
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1
        for key, value in frequency.items():
            if value > 1:
                result.append(key)
        if not result:
            return [-1]
        result.sort()
        return result

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends