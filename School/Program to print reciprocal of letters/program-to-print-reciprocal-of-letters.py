#User function Template for python3
class Solution:
    def reciprocalString(self, S):
        # code here
        res = ""
        for letter in S:
            if letter >= "A" and letter <= "Z":
                res += chr(90 - (ord(letter) - 65))
            elif letter >= "a" and letter <= "z":
                res += chr(122 - (ord(letter) - 97))
            else:
                res += letter
        
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.reciprocalString(S))
# } Driver Code Ends