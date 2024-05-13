//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

class Matrix {
  public:
    template <class T>
    static void input(vector<vector<T>> &A, int n, int m) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf("%d ", &A[i][j]);
            }
        }
    }

    template <class T>
    static void print(vector<vector<T>> &A) {
        for (int i = 0; i < A.size(); i++) {
            for (int j = 0; j < A[i].size(); j++) {
                cout << A[i][j] << " ";
            }
            cout << endl;
        }
    }
};


// } Driver Code Ends

class Solution {
  public:
    int MinimumEffort(int rows, int columns, vector<vector<int>> &heights) {
    int n=heights.size(),m=heights[0].size();
        vector<vector<int>>dp(n,vector<int>(m,INT_MAX));
        dp[0][0]=0;
        queue<pair<int,int>>q;
        q.push({0,0});
        int dx[4]={1,-1,0,0};
        int dy[4]={0,0,1,-1};
        while(!q.empty()){
            pair<int,int>curr=q.front();
            q.pop();
            int x=curr.first;
            int y=curr.second;
            for(int k=0;k<4;k++){
            int nx=x+dx[k] ,ny=y+dy[k];
            if(nx<0||ny<0||nx>=n||ny>=m||dp[nx][ny]<=dp[x][y]) continue;
            dp[nx][ny]=min(max(dp[x][y],abs(heights[nx][ny]-heights[x][y])),dp[nx][ny]);
            q.push({nx,ny});
            }
        }
    return dp[n-1][m-1];
    
    }};

//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {

        int rows;
        scanf("%d", &rows);

        int columns;
        scanf("%d", &columns);

        vector<vector<int>> heights(rows, vector<int>(columns));
        Matrix::input(heights, rows, columns);

        Solution obj;
        int res = obj.MinimumEffort(rows, columns, heights);

        cout << res << endl;
    }
}

// } Driver Code Ends