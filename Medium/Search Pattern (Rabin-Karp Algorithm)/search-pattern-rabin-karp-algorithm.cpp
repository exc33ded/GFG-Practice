//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution
{
    public:
    vector<int> search(string pattern, string text) {
        vector<int> ans;

        for (int i = 0; i <= text.length() - pattern.length(); ++i) {
            int j = 0; 

            while (j < pattern.length() && text[i + j] == pattern[j]) {
                ++j; 
            }

  
            if (j == pattern.length()) {
                ans.push_back(i + 1); 
            }
        }

        return ans;
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string S, pat;
        cin >> S >> pat;
        Solution ob;
        vector <int> res = ob.search(pat, S);
        for (int i : res) cout << i << " ";
        cout << endl;
    }
    return 0;
}

// Contributed By: Pranay Bansal

// } Driver Code Ends