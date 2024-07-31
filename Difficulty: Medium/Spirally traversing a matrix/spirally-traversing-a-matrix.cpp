//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    vector<int> spirallyTraverse(vector<vector<int> > &matrix) {
        vector<int> result;
        if(matrix.empty()) return result;
        
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        int top = 0, bottom = rows - 1;
        int left = 0, right = cols - 1;
        
        while(top <= bottom && left <= right) {
            // Traverse from left to right on the topmost row
            for(int i = left; i <= right; i++) {
                result.push_back(matrix[top][i]);
            }
            top++;
            
            // Traverse from top to bottom on the rightmost column
            for(int i = top; i <= bottom; i++) {
                result.push_back(matrix[i][right]);
            }
            right--;
            
            // Make sure we are now on a different row
            if(top <= bottom) {
                // Traverse from right to left on the bottommost row
                for(int i = right; i >= left; i--) {
                    result.push_back(matrix[bottom][i]);
                }
                bottom--;
            }
            
            // Make sure we are now on a different column
            if(left <= right) {
                // Traverse from bottom to top on the leftmost column
                for(int i = bottom; i >= top; i--) {
                    result.push_back(matrix[i][left]);
                }
                left++;
            }
        }
        
        return result;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;

    while (t--) {
        int r, c;
        cin >> r >> c;
        vector<vector<int>> matrix(r, vector<int>(c, 0));

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> matrix[i][j];
            }
        }

        Solution ob;
        vector<int> result = ob.spirallyTraverse(matrix);
        for (int i = 0; i < result.size(); ++i)
            cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends