//{ Driver Code Starts


#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution {
public:
    int FindCoverage(vector<vector<int>>&matrix){
    int count = 0;
    int m = matrix.size(), n = matrix[0].size();
    for(int i=0; i<m; i++) {
        for(int j=0; j<n; j++) {
            if(matrix[i][j] == 0) {
                if(j < n-1 && matrix[i][j+1] == 1) 
                    ++count;
                if(j > 0 && matrix[i][j-1] == 1) 
                    ++count;
                if(i < m-1 && matrix[i+1][j] == 1) 
                    ++count;
                if(i > 0 && matrix[i-1][j] == 1) 
                    ++count;
            }
        }
    }
    return count;
}
};


//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<int>>matrix(n, vector<int>(m, 0));
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				cin >> matrix[i][j];
		Solution obj;
		int ans = obj.FindCoverage(matrix);
		cout << ans << "\n";
	}
	return 0;
}
// } Driver Code Ends