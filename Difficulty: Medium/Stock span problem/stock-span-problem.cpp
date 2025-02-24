//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    vector<int> calculateSpan(vector<int>& arr) {
        vector<int>ans(arr.size(),1);
        stack<pair<int,int>>st;
        st.push({arr[arr.size()-1],arr.size()-1});
        for(int i =arr.size()-2;i>=0;i--){
            
            if(arr[i]<=st.top().first)st.push({arr[i],i});
            else{
                while(!st.empty()&&st.top().first<arr[i]){
                    ans[st.top().second]=st.top().second-i;
                    st.pop();
                }
                st.push({arr[i],i});
            } 
            
        
        }
        while(!st.empty()&&st.top().first<INT_MAX){
                    ans[st.top().second]=st.top().second-(-1);
                    st.pop();
        }
        return ans;
        
    }
};

//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution obj;
        vector<int> ans = obj.calculateSpan(arr);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends