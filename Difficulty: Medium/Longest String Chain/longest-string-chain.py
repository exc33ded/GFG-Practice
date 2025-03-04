#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def longestStringChain(self, words):
        # Code here
        words.sort(key=len) 
        word_map = {}  
        max_chain = 1  
        
        for word in words:
            word_map[word] = 1  
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]  
                if predecessor in word_map:
                    word_map[word] = max(word_map[word], word_map[predecessor] + 1)
            max_chain = max(max_chain, word_map[word])  # Update the maximum chain length
        
        return max_chain


        


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends