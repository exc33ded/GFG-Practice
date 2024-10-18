//{ Driver Code Starts
#include <iostream>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    string roundToNearest(string str) {
        // Complete the function
         int n=str.length(),a;
        if(str[n-1]<='5')
            str[n-1]='0';
        else
        {
            str[n-1]='0';
           for(int i=n-2;i>=0;i--)
           {
               a=(int)str[i]-'0';
               a+=1;
               if(a!=10)
               {
                   str[i]=(str[i]+1);
                   return str;
               }
               str[i]='0';
           }
           str='1'+str;
        }
        return str;
    }
};

//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    while (t--) {
        string str;
        cin >> str;
        Solution ob;
        cout << ob.roundToNearest(str) << endl;
    }

    return 0;
}
// } Driver Code Ends