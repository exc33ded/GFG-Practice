class Solution:
    def median(self, mat):
    	# code here 
    	a=[]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                a.append(mat[i][j])
        a.sort()
        l=0
        r=len(a)-1
        res=(l+r)//2
        return a[res]
    	