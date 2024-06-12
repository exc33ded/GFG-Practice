//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution
{
    public:
 int padovanSequence(int n)
    {
       //code here
        if (n == 0 || n == 1 || n == 2) {
            return 1;
        }
        

        int pPrevPrev = 1; 
        int pPrev = 1;     
        int pCurr = 1;     
        
       
        for (int i = 3; i <= n; i++) {
            int pNext = (pPrevPrev + pPrev) % 1000000007; 
            pPrevPrev = pPrev;
            pPrev = pCurr;
            pCurr = pNext;
        }
        
        return pCurr;
    }};


//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
    	int n;
    	cin>>n;
    	Solution ob;
    	cout<<ob.padovanSequence(n)<<endl;
    }
    return 0;
}
// } Driver Code Ends