# Deletion of elements at different positions. 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print('list is empty')
        else:
            temp=self.head
            while temp:
                print(temp.data," ",end="")
                temp=temp.next
            print('\n')
                
    def insert(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=n
    def first_delete(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    def end_delete(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def pos_delete(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
l=Linkedlist()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.display()
l.first_delete()
#l.display()
l.end_delete()
l.pos_delete(2)
l.display()