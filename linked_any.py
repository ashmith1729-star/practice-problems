class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertmid(head,x,y):
    newnode=Node(x)
    if x==1:
        newnode=head
        return newnode
    else:
        count=head
        i=1
        for i in range(i,y-1):
            count=count.next
        newnode.next=count.next
        count.next=newnode
    return head
node0=Node(1)
node1=Node(2)
node2=Node(4)
node3=Node(5)
head=node0
node0.next=node1
node1.next=node2
node2.next=node3
head=insertmid(head,3,3)
current=head
while current:
    print(current.data,end="->")
    current=current.next
print("None")    
