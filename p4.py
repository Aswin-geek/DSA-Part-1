class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data," ",end="")
                temp=temp.next
                
l=DLL()
n1=Node(1)
l.head=n1
n2=Node(2)
n1.next=n2
n2.prev=n1
n3=Node(3)
n2.next=n3
n3.prev=n2
l.display()