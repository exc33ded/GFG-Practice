//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
/* The function returns 1 if
IP string is valid else return 0
You are required to complete this method */
class Solution {
  public:
    int isValid(string s) {
        // code here
        int i=0;
        string temp="";
        int cnt=3;
        while(cnt){
            if(s[i]!='.'){
                temp=temp+s[i];
            }
            else{
                int no=stoi(temp);
                if(no<0||no>255)return 0;
                temp="";
                cnt--;
            }
            i++;
        }
        temp="";
        while(i<s.size()){
            temp+=s[i];
            i++;
        }
        int no=stoi(temp);
        if(no<0||no>255)return 0;
        else 1;
    }
};

//{ Driver Code Starts.

int main() {
    // your code goes here
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        // if (s.size() == 3) {
        //     cout << "false" << endl;
        //     return 0;
        // }
        Solution ob;
        bool f = ob.isValid(s);
        if (f)
            cout << "true" << endl;
        else
            cout << "false" << endl;
    }
    return 0;
}
// } Driver Code Ends