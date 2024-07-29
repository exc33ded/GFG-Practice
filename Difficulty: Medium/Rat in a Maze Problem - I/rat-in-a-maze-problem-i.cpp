//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution {
  public:
    bool isSafe(int newx, int newy, vector<vector<int>> &mat, vector<vector<bool>> &visited, int n){
        // outoff bound
        if ((newx < 0 || newy < 0) || (newx >= n || newy >= n))
        {
            return false;
        }
        // already visited
        if (visited[newx][newy] == true)
        {
            return false;
        }
        // blocked space
        if (mat[newx][newy] == 0)
        {
            return false;
        }
        // valid case
        return true;
    }
    
    void solve(vector<vector<int>> &mat, vector<vector<bool>> &visited, int n, vector<string> &ans, int srcX, int srcY, int desX, int desY, string output){
        //   base case
        if(srcX == desX && srcY == desY){
            // rat reached the destination
            // string output store in ans
            ans.push_back(output);
            return;
        }
        
        // handle the 1 case
        // 1 case -> UP , DOWN, LEFT , RIGHT
        // UP
        // i, j -> (i-1, j)
        int newx = srcX-1;
        int newy = srcY;
        if(isSafe(newx, newy, mat, visited, n)){
            visited[newx][newy] = true;
            solve(mat, visited, n, ans, newx, newy, desX, desY, output+'U');
            visited[newx][newy] = false;
        }
        
        // LEFT
        // i, j -> (i. j-1)
        newx = srcX;
        newy = srcY-1;
        if(isSafe(newx, newy, mat, visited, n)){
            visited[newx][newy] = true;
            solve(mat, visited, n, ans, newx, newy, desX, desY, output+'L');
            visited[newx][newy] = false;
        }
        
        // DOWN
        // i, j -> (i+1, j)
        newx = srcX+1;
        newy = srcY;
        if(isSafe(newx, newy, mat, visited, n)){
            visited[newx][newy] = true;
            solve(mat, visited, n, ans, newx, newy, desX, desY, output+'D');
            visited[newx][newy] = false;
        }
        
        // RIGHT
        // i, j -> (i, j+1)
        newx = srcX;
        newy = srcY+1;
        if(isSafe(newx, newy, mat, visited, n)){
            visited[newx][newy] = true;
            solve(mat, visited, n, ans, newx, newy, desX, desY, output+'R');
            visited[newx][newy] = false;
        }
    }
    
    vector<string> findPath(vector<vector<int>> &mat) {
        int n = mat.size();
        
        vector<string> ans;
        vector<vector<bool>> visited(n, vector <bool>(n, false));
        
        int srcX = 0;
        int srcY = 0;
        visited[0][0] = true;
        int desX = n-1;
        int desY = n-1;
        
        string output = "";
        
        if(mat[0][0] == 0){
            return ans;
        }
        
        solve(mat, visited, n, ans, srcX, srcY, desX, desY, output);
        
        return ans;
    }
};



//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> m(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> m[i][j];
            }
        }
        Solution obj;
        vector<string> result = obj.findPath(m);
        sort(result.begin(), result.end());
        if (result.size() == 0)
            cout << -1;
        else
            for (int i = 0; i < result.size(); i++)
                cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends