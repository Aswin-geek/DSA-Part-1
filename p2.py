# Insertion of elements at different positions. 
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
                print(temp.data)
                temp=temp.next
    def insert(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=n
    def insert_first(self,data):
        n=Node(data)
        n.next=self.head
        self.head=n
    def insert_pos(self,data,pos):
        n=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        n.next=temp.next
        temp.next=n
l=Linkedlist()
l.insert(10)
l.insert(20)
l.insert_first(5)
l.insert_first(3)
l.insert_pos(12,2)       
l.display()