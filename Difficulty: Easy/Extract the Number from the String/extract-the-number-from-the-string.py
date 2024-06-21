class Solution:
    def ExtractNumber(self,sentence):
        #code here
        l = []
        x = []
        a = S.split(" ")
        for i in a:
            if i.isdigit():
                l.append(i)
        for j in l:
            if "9" not in j:
                x.append(int(j))
        if x:
            return max(x)
        else:
            return -1


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends