class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertbegin(head,x):
    newnode=Node(x)
    newnode.next=head
    return newnode
node1=Node(2)
node2=Node(3)
node3=Node(4)
head=node1
node1.next=node2
node2.next=node3
head=insertbegin(head,1)
head=insertbegin(head,0)
current=head
while current:
    print(current.data,end="->")
    current=current.next
print("None")    
