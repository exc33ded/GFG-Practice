//{ Driver Code Starts
import java.util.*;

class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}

public class Main {
    public static void printList(Node node) {
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();

        while (t-- > 0) {
            List<Integer> arr = new ArrayList<>();
            String input = sc.nextLine();
            Scanner ss = new Scanner(input);

            while (ss.hasNextInt()) {
                arr.add(ss.nextInt());
            }

            Node head = new Node(arr.get(0));
            Node tail = head;

            for (int i = 1; i < arr.size(); ++i) {
                tail.next = new Node(arr.get(i));
                tail = tail.next;
            }

            Solution ob = new Solution();
            Node[] result = ob.alternatingSplitList(head);
            printList(result[0]);
            printList(result[1]);
        }

        sc.close();
    }
}

// } Driver Code Ends


// User function Template for Java
/*
struct Node
{
    int data;
    struct Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }

};
*/

class Solution {
    // Function to append a new node with newData at the end of a linked list
    Node[] alternatingSplitList(Node head) {
        // code here
     Node dummy1 = new Node(0);
        Node dummy2 = new Node(0);
        
        // Pointers to the current nodes of the two lists
        Node list1 = dummy1;
        Node list2 = dummy2;
        
        // Boolean flag to alternate between the two lists
        boolean alternate = true;
        
        while (head != null) {
            if (alternate) {
                list1.next = head;
                list1 = list1.next;
            } else {
                list2.next = head;
                list2 = list2.next;
            }
            
            // Move to the next node
            head = head.next;
            
            // Alternate the flag
            alternate = !alternate;
        }
        
        // Terminate the two lists
        list1.next = null;
        list2.next = null;
        
        // Return the heads of the two lists (excluding dummy nodes)
        return new Node[] {dummy1.next, dummy2.next};
    }
}
