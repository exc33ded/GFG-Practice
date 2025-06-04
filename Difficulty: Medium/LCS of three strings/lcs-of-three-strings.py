class Solution:
    def lcsOf3(self,s1, s2, s3):
        n1,n2,n3=len(s1),len(s2),len(s3)
        dp=[[[None]*(n3+1) for _ in range(n2+1)] for _ in range(2)]
        for i in range(n1+1):
            for j in range(n2+1):
                for k in range(n3+1):
                    if i==0 or j==0 or k==0:
                        dp[1][j][k]=0
                    elif s1[i-1]==s2[j-1]==s3[k-1]:
                        dp[1][j][k]=1+dp[0][j-1][k-1]
                    else:
                        dp[1][j][k]=max(dp[0][j][k],dp[1][j-1][k],dp[1][j][k-1])
            dp[0],dp[1]=dp[1],dp[0]
        return dp[0][n2][n3]