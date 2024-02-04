#User function Template for python3

# Definition for singly-linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definition for singly-linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

class Solution:
    def subLinkedList(self, l1, l2): 
        # Helper function to convert linked list to number
        def linkedListToNumber(head):
            num = ""
            curr = head
            while curr:
                num += str(curr.data)
                curr = curr.next
            return int(num)

        # Code to find the absolute difference of two linked lists
        num1 = linkedListToNumber(l1)
        num2 = linkedListToNumber(l2)
        
        # Calculate the absolute difference
        res = abs(num1 - num2)
        
        # Convert the result to a list of digits
        digits = [int(digit) for digit in str(res)]
        
        # Create a dummy node for the result linked list
        dummy = Node(-1)
        curr = dummy
        
        # Populate the result linked list with digits
        for digit in digits:
            curr.next = Node(digit)
            curr = curr.next
        
        return dummy.next
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end='')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        ob = Solution()
        res = ob.subLinkedList(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends