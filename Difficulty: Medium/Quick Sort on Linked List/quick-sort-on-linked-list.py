#User function Template for python3

def quickSort(head):
    #return head after sorting
    if not head: #base case: list is empty
        return None
    pivot = head #taking pivot as head instead of last value as suggested by GfG saves steps
    head = pivot.next #excluding the pivot from the comparisons
    lh = lt = rh = rt = None #left-head, left-tail, right-head, right-tail for the two linked lists
    while head:
        if head.data < pivot.data:
            if not lh:
                lh = lt = head
            else:
                lt.next = head
                lt = lt.next
        else:
            if not rh:
                rh = rt = head
            else:
                rt.next = head
                rt = rt.next
        head = head.next
    if rh:
        rt.next = None #Since we have directly added the nodes to the linked lists, it is possible that the last element.next had some other value that was included in the "left" linked list. This is to ensure that the right linked list terminates.
    pivot.next = quickSort(rh) #sorting the right linked list and adding it to the right of pivot.
    if lh:
        lt.next = None
        lt = lh = quickSort(lh)
        while lt.next:
            lt = lt.next
        lt.next = pivot
        return lh
    return pivot #no element to the left of pivot, so the pivot itself is the head of the sorted list

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
from collections import defaultdict


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:

    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def nodeID(head, dic):
    while head:
        dic[head.data].append(id(head))
        head = head.next


def printList(head, dic):
    while head:
        if id(head) not in dic[head.data]:
            print("Do'nt swap data, swap pointer/node")
            return
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        dic = defaultdict(list)  # dictonary to keep data and id of node
        nodeID(ll.head, dic)  # putting data and its id

        resHead = quickSort(ll.head)
        printList(resHead, dic)  #verifying and printing
        print()

        print("~")

# } Driver Code Ends