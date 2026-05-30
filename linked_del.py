class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def delend(head):
    last=head
    while last.next.next is not None:
        last=last.next
    last.next=None
    return head
def delbegin(head):
    return head.next
def delany(head,z):
    if z==1:
        return head.next
    else:
        last=head
        for i in range(1,z-1):
            last=last.next
        last.next=last.next.next
    return head

node1=Node(15)
node2=Node(56)
node3=Node(73)
node4=Node(345)
node5=Node(342)
node6=Node(8234)
node7=Node(143)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7

head=node1
current =head
print("Before")
while current:
    print(current.data,end="->")
    current=current.next
print("None")

head=delend(head)
head=delbegin(head)
head=delany(head,3)
current =head
print("After")
while current:
    print(current.data,end="->")
    current=current.next
print("None")