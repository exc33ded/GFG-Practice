//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int findSubString(string& str) {
        // code here
        unordered_map<char,int>mp;
        unordered_set<char>s;
        int ans=str.length()+1;
        for(auto &ch:str){
            s.insert(ch);
        }
        for(int i=0;i<str.length();i++){
            mp[str[i]]=i;
            
            if(mp.size()==s.size()){
                int mn=str.size()+1;
                int mx=0;
                for(auto &m:mp){
                    mn=min(mn,m.second);
                    mx=max(mx,m.second);
                }
                ans=min(ans,mx-mn+1);
            }
        }
        return ans;
    }
};


//{ Driver Code Starts.
//      Driver code
int main() {
    int t;
    cin >> t;
    while (t--) {

        string str;
        cin >> str;
        Solution ob;
        cout << ob.findSubString(str) << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends