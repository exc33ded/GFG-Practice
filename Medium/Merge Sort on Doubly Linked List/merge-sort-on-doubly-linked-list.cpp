//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    struct Node *next, *prev;

    Node(int x) {
        data = x;
        next = NULL;
        prev = NULL;
    }
};


// } Driver Code Ends

/* Structure of the node of the list is as
struct Node
{
    int data;
    struct Node *next, *prev;
    Node (int x){
        data = x;
        next = prev = NULL;
    }
};
*/

class Solution {
  public:
    // Function to sort the given doubly linked list using Merge Sort.
   Node* getMiddle(Node* head){
    Node* slow = head;
    Node* fast = head;
    while(fast->next && fast->next->next) {
        slow= slow->next;
        fast=fast->next->next;
    }
    return slow;
}
Node* merge(Node* left, Node* right) {
    if(left==NULL) return right;
    if(right==NULL) return left;
    Node* ans = new Node(-1);
    Node* temp = ans;
    while(left&&right) {
        if(left->data < right->data) {
            temp->next = left;
            left->prev = temp;
            temp = left;
            left = left->next;
        }
        else {
            temp->next = right;
            right->prev = temp;
            temp = right;
            right = right->next;
        }
    }
    while(left) {
        temp->next = left;
        left->prev = temp;
        temp = left;
        left = left->next;
    }
    while(right) {
        temp->next = right;
        right->prev = temp;
        temp = right;
        right = right->next;
    }
    ans = ans->next;
    ans->prev = NULL;
    return ans;
}
struct Node *sortDoubly(struct Node *head)
{
    if(head==NULL || head->next==NULL) {
        return head;
    }
    Node*mid = getMiddle(head);
    Node* left = head;
    Node* right = mid->next;
    mid->next = NULL;
    left = sortDoubly(left);
    right = sortDoubly(right);
    
    Node* ans = merge(left,right);
    return ans;
}
};


//{ Driver Code Starts.

void insert(struct Node **head, int data) {
    struct Node *temp = new Node(data);
    if (!(*head))
        (*head) = temp;
    else {
        temp->next = *head;
        (*head)->prev = temp;
        (*head) = temp;
    }
}

void print(struct Node *head) {
    struct Node *temp = head;
    while (head) {
        cout << head->data << ' ';
        temp = head;
        head = head->next;
    }
    cout << endl;
    while (temp) {
        cout << temp->data << ' ';
        temp = temp->prev;
    }
    cout << endl;
}

// Utility function to swap two integers
void swap(int *A, int *B) {
    int temp = *A;
    *A = *B;
    *B = temp;
}

// Driver program
int main(void) {
    long test;
    cin >> test;
    while (test--) {
        int n, tmp;
        struct Node *head = NULL;
        cin >> n;
        while (n--) {
            cin >> tmp;
            insert(&head, tmp);
        }
        Solution ob;
        head = ob.sortDoubly(head);
        print(head);
    }
    return 0;
}

// } Driver Code Ends