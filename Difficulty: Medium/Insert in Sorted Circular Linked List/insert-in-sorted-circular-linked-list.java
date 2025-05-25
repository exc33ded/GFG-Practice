/*
class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
} */


class Solution 
{
    public Node sortedInsert(Node head, int data) 
    {
        // code here
        Node newNode=new Node(data);
        Node dummy=null;
        if(head==null)
        {
             newNode.next=newNode;
             return newNode;
        }
         
        Node tail=null;
        Node temp=head;
        
        while(temp.next!=head)
        {
            if(temp.data<=data && temp.next.data>data)
            {
                dummy=temp.next;
                temp.next=newNode;
                newNode.next=dummy;
                return head;
            }
            temp=temp.next;
        }
       temp.next=newNode;
       newNode.next=head;
       
       if(data<head.data){
           head=newNode;
       }
       return head;
    }
}