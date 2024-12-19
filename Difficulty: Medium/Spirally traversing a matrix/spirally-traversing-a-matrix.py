class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        m, n = len(mat), len(mat[0])

    # List to store the spiral order elements
        res = []
    
        # Initialize boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1
    
        # Iterate until all elements are printed
        while top <= bottom and left <= right:
    
            # Print top row from left to right
            for i in range(left, right + 1):
                res.append(mat[top][i])
            top += 1
    
            # Print right column from top to bottom
            for i in range(top, bottom + 1):
                res.append(mat[i][right])
            right -= 1
    
            # Print bottom row from right to left (if exists)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(mat[bottom][i])
                bottom -= 1
    
            # Print left column from bottom to top (if exists)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1
    
        return res

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends