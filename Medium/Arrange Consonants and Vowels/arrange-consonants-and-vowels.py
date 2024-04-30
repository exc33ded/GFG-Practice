#User function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
        if(head.next == None):
            return head
        v = []
        c = []
        length = 0
        vow = "aeiou"
        temp = head
        while(temp):
            if(temp.data in vow):
                v.append(temp.data)
            else:
                c.append(temp.data)
            temp = temp.next
            length += 1
            
        if(length == len(v)):
            return head
            
        elif(length == len(c)):
            return head
        
        else:
            l = v + c
            temp = head
            i = 0
            while(temp):
                temp.data = l[i]
                temp = temp.next
                i += 1
            
        return head


#{ 
 # Driver Code Starts


# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends