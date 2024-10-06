//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        scanner.nextLine();
        Solution soln = new Solution();
        while (t-- > 0) {
            Node head = null;
            String input = scanner.nextLine();
            Scanner ss = new Scanner(input);
            List<Integer> arr = new ArrayList<>();
            while (ss.hasNextInt()) {
                arr.add(ss.nextInt());
            }
            int n = arr.size();
            for (int i = 0; i < n; i++) {
                int tmp = arr.get(i);
                head = soln.insert(head, tmp);
            }

            ArrayList<Integer> list = soln.getList(head);
            for (int x : list) System.out.print(x + " ");
            System.out.println();

            for (int i = list.size() - 1; i >= 0; i--) {
                System.out.print(list.get(i) + " ");
            }
            System.out.println();
        }
    }
}

class Node {
    int data;
    Node npx;

    Node(int x) {
        data = x;
        npx = null;
    }
}

// } Driver Code Ends


// class Node {
//     int data;
//     Node npx;

//     Node(int x) {
//         data = x;
//         npx = null;
//     }
// }
class Solution {
    // function should insert the data to the front of the list
    static Node insert(Node head, int data) {
        Node newNode = new Node(data);
        newNode.npx = head;
        return newNode;
    }

    // function to get the list of integers from the linked list
    static ArrayList<Integer> getList(Node head) {
        ArrayList<Integer> list = new ArrayList<>();
        Node current = head;
        while (current != null) {
            list.add(current.data);
            current = current.npx;
        }
        return list;
    }

    // function to compute the XOR of all elements in the list
    static int compute(ArrayList<Integer> list) {
        int xor = 0;
        for (int num : list) {
            xor ^= num;
        }
        return xor;
    }
}