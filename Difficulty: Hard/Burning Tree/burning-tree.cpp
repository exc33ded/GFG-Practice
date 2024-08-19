//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};


Node *buildTree(string str) {
    // Corner Case
    if (str.length() == 0 || str[0] == 'N')
        return NULL;

    // Creating vector of strings from input
    // string after spliting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str; iss >> str;)
        ip.push_back(str);

    // Create the root of the tree
    Node *root = new Node(stoi(ip[0]));

    // Push the root to the queue
    queue<Node *> queue;
    queue.push(root);

    // Starting from the second element
    int i = 1;
    while (!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node *currNode = queue.front();
        queue.pop();

        // Get the current Node's value from the string
        string currVal = ip[i];

        // If the left child is not null
        if (currVal != "N") {

            // Create the left child for the current Node
            currNode->left = new Node(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->left);
        }

        // For the right child
        i++;
        if (i >= ip.size())
            break;
        currVal = ip[i];

        // If the right child is not null
        if (currVal != "N") {

            // Create the right child for the current Node
            currNode->right = new Node(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}


// } Driver Code Ends
//User function Template for C++

/*
struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/
class Solution {
  public:
  
    Node* find_parent(Node* root,int target,unordered_map<Node*,Node*>&parent_tracker){
        queue<Node*>q;
        q.push(root);
         Node*res=NULL;
        while(!q.empty()){
            Node*curr=q.front();
            if(curr->data==target){
                res=curr;
            }
            q.pop();
            if(curr->left){
                q.push(curr->left);
                parent_tracker[curr->left]=curr;
            }
            if(curr->right){
                q.push(curr->right);
                parent_tracker[curr->right]=curr;
            }
        }
       return res; 
    }
    int minTime(Node* root, int target) 
    {
       unordered_map<Node*,Node*>parent_tracker;
       Node*res= find_parent(root,target,parent_tracker);
       unordered_map<Node*,bool>visited;
       queue<Node*>q;
       q.push(res);
       visited[res]=true;
    
       int time=0;
       while(!q.empty()){
            bool check=false;
           int size=q.size();
           for(int i=0;i<size;i++){
               Node* node=q.front();
               q.pop();
               if(node->left && visited[node->left]==false){
                   q.push(node->left);
                   visited[node->left]=true;
                   check=true;
               }
                 if(node->right && visited[node->right]==false){
                   q.push(node->right);
                   visited[node->right]=true;
                   check=true;
               }
               if(parent_tracker[node] && visited[parent_tracker[node]]==false){
                  visited[parent_tracker[node]]=true;
                   q.push(parent_tracker[node]);
                   check=true;
               }
            }
            if(check==true)time++;
       }
       return time;
     }
};



//{ Driver Code Starts.

int main() 
{
    int tc;
    scanf("%d ", &tc);
    while (tc--) 
    {    
        string treeString;
        getline(cin, treeString);
        // cout<<treeString<<"\n";
        int target;
        cin>>target;
        // cout<<target<<"\n";

        Node *root = buildTree(treeString);
        Solution obj;
        cout<<obj.minTime(root, target)<<"\n"; 

        cin.ignore();

    }


    return 0;
}

// } Driver Code Ends