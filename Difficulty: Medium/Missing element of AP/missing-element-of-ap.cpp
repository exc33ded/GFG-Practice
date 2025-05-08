//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++

class Solution {
  public:
    int findMissing(vector<int> &arr) {
        //Assume the difference
        int assumedDiff = arr[1] - arr[0];
        int voteCount = 1;
        
        // Boyer Moore Majority Voting Algorithm to find the actual common difference
        for(int i = 1; i < arr.size() - 1; ++i) {
            int currentDiff = arr[i + 1] - arr[i];

            if(currentDiff == assumedDiff) {
                voteCount++;
            }
            else {
                voteCount--;
            }

            if(voteCount == 0) {
                assumedDiff = currentDiff;
                voteCount = 1;
            }
        }

        //Find the missing number
        for(int i = 1; i < arr.size(); ++i) {
            if(arr[i] - arr[i - 1] != assumedDiff) {
                return arr[i - 1] + assumedDiff;
            }
        }
    
        //Return the next number in sequence if not found in the array
        return arr.back() + assumedDiff;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;

        getline(cin, input);

        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution ob;
        cout << ob.findMissing(arr) << "\n";
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends