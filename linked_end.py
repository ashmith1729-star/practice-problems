class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertend(head,x):
    newnode=Node(x)
    last=head
    while last.next is not None:
        last=last.next
    last.next=newnode
    return head
node1=Node(1)
node2=Node(2)
node3=Node(3)
head=node1
node1.next=node2
node2.next=node3
current=head
insertend(head,4)
while current:
    print(current.data,end="->")
    current=current.next
print("None")    

        