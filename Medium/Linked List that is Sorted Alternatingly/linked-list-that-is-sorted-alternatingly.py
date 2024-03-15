#User function Template for python3


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def sort(self, h1):
        even=[h1]
        odd=[]
        cur=h1.next
        while cur:
            if len(even)>len(odd):
                odd.append(cur)
            else:
                even.append(cur)
            cur=cur.next
        even=even[::-1]
        head=Node(0)
        cur=head
        while odd or even:
            if odd and even:
                if odd[-1].data<=even[-1].data:
                    tmp=odd.pop()
                else:
                    tmp=even.pop()
            elif odd:
                tmp=odd.pop()
            else:
                tmp=even.pop()
            cur.next=tmp
            cur=cur.next
        cur.next=None
        return head.next


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
        
        ob = Solution()
        resHead=ob.sort(ll1.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends