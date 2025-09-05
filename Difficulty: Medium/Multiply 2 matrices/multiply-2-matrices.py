class Solution:
	def multiply(self, matrixA, matrixB):
		# Code here
		full_matrix = [[sum(a * b for a, b in zip(matrixA, matrixB))for matrixB in zip(*matrixB)]for matrixA in matrixA]
        for i in range(0,n):
            for j in range(0,n):
                matrixA[i][j]=full_matrix[i][j]
		
		return matrixA