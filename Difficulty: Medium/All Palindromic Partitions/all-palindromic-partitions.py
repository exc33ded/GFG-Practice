class Solution:
    def isPalindrome(self,s):
        l,h=0,len(s)-1
        while l<h:
            if s[l]!=s[h]:
                return False
            l+=1
            h-=1
        return True

    def solve(self,s,ans,start,path):
        if start==len(s):
            ans.append(path[:])
        for end in range(start+1,len(s)+1):
            subStr=s[start:end]
            if self.isPalindrome(subStr):
                path.append(subStr)
                self.solve(s,ans,end,path)
                path.pop()
    
    def palinParts (self, s):
        ans=[]
        self.solve(s,ans,0,[])
        return ans

