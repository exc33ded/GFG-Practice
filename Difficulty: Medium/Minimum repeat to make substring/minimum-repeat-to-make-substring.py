#User function Template for python3

class Solution:
    def minRepeats(self, s1, s2):
        # code here 
        if len(set(s1))<len(set(s2)):
            return -1
        l1=len(s1)
        if s2.find(s1)==0:
            ret=0
            while s2.find(s1)==0:
                s2=s2[l1:]
                ret+=1
            if s2=='':
                return ret
            return ret+1 if s2 in s1[:len(s2)] else -1
        import re
        ret=0
        while s2.find(s1)>0:
            l2=len(s2)
            s2=re.sub(s1,'',s2)
            ret+=(l2-len(s2))//l1
        if s2:
            l2=len(s2)
            s1=s1*2
            if s2 in s1:
                return ret+2
            return -1
        return ret


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))

# } Driver Code Ends