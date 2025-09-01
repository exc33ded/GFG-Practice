/*
class Node {
  public:
    int data;
    Node *next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};
*/
class Solution {
  public:
    Node* swapKth(Node* head, int k) {
        // code here
        if(head==NULL) return NULL;
        Node *curr1 = head, *curr2 = head, *temp = head;
        int cnt = 0;
        
        while(temp!=NULL){
            cnt++;
            temp = temp->next;
        }
        
        if(cnt<k) return head;
        if(2*k -1 == cnt) return head;
        
        for(int i =1; i<k ; i++){
            curr1 = curr1 ->next;
        }
        for(int j = 1; j<cnt-k +1 ; j++){
            curr2 = curr2->next;
        }
        int val = curr1->data;
        curr1 ->data = curr2->data;
        curr2->data = val;
        return head;
    }
};

