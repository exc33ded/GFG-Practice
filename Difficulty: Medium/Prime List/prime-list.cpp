//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

class Node {
  public:
    int val;
    Node* next;

    Node(int x) {
        val = x;
        next = NULL;
    }
};

void printList(Node* node) {
    while (node != NULL) {
        cout << node->val << " ";
        node = node->next;
    }
    cout << "\n";
}


// } Driver Code Ends

// User function Template for C++

/*
class Node{
public:
    int val;
    Node *next;
    Node(int num){
        val=num;
        next=NULL;
    }
};
*/

class Solution {
  public:
    vector<int>sieveof(int max){
        vector<bool>pr(max,true);
        vector<int>primes;
        pr[0]=false;
        pr[1]=false;
        for(int i=2;i*i<=max;i++){
            if(pr[i]){
                for(int p=i*i;p<=max;p+=i){
                    pr[p]=false;
                }
            }
        }
        
        for(int i=2;i<=max;i++){
            if(pr[i]){
                primes.push_back(i);
            }
        }
        return primes;
    }
    Node *primeList(Node *head) {
        // code here
        // sieve +binary search?
        int max=1e4+100;
        vector<int>seive=sieveof(max);
        
        Node* temp=head;
        while(temp){
            int curr=temp->val;
            auto it=lower_bound(seive.begin(),seive.end(),curr);
            if(it==seive.begin()){
                temp->val=*it;
            }
            else{
                int x=*it;
                auto it2=--it;
                int y=*it2;
                //cout<<y<<" "<<x<<endl;
                if((curr-y)>(x-curr)){
                    temp->val=x;
                }
                else{
                    temp->val=y;
                }
            }
            temp=temp->next;
        }
        return head;
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

        if (arr.empty()) {
            cout << -1 << endl;
            continue;
        }

        int data = arr[0];
        struct Node* head = new Node(data);
        struct Node* tail = head;
        for (int i = 1; i < arr.size(); ++i) {
            data = arr[i];
            tail->next = new Node(data);
            tail = tail->next;
        }

        Solution ob;
        head = ob.primeList(head);
        printList(head);
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends