class Solution:
	def isWordExist(self, mat, word):
		#Code here
        rows, cols = len(mat), len(mat[0])
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols or mat[i][j] != word[index]:
                return False
            
            temp = mat[i][j]
            mat[i][j] = '#'  # Mark as visited
            
            # Explore all 4 directions
            found = (dfs(i + 1, j, index + 1) or 
                     dfs(i - 1, j, index + 1) or 
                     dfs(i, j + 1, index + 1) or 
                     dfs(i, j - 1, index + 1))
            
            mat[i][j] = temp  # Restore original character
            return found
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == word[0]:  # Start DFS if first character matches
                    if dfs(i, j, 0):
                        return True
        
        return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends