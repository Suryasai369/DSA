class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def read(self,index):
        current_node=self.head
        current_index=0
        while current_index < index:
            current_node = current_node.next
            current_index+=1
        return current_node.data
    
    def search(self,data):
        current_node = self.head
        current_index = 0
        while current_node!=None:
            if current_node.data == data:
                return current_index
            current_node = current_node.next
            current_index+=1
        return "Not Found"
    
    def insert_at_index(self,index,value):
        current_node=self.head
        current_index=0
        while current_node!=None and current_index < index:
            current_node = current_node.next
            current_index+=1
        if current_node!=None:
            new_node=Node(value)
            new_node.next = current_node.next
            current_node.next=new_node
        else:
            return "Index not found"
        
    def insert_end(self,value):
        current_node=self.head
        while current_node.next!=None:
            current_node=current_node.next
        node = Node(value)
        current_node.next = node

    def insert_beg(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
        
    def delete_at_index(self,index):
        current_node=self.head
        current_index=0
        while current_index < index and current_node!=None and current_node.next!=None:
            current_node = current_node.next
            current_index+=1
        if current_node!=None and current_node.next!=None:
            current_node.next = current_node.next.next
    
    def delete_at_beg(self):
        current_node=self.head
        self.head = current_node.next

    def delete_at_end(self):
        current_node=self.head
        while current_node.next.next!=None:
            current_node=current_node.next
        current_node.next=None
        
    def pr(self):
        current_node=self.head
        while current_node!=None:
            print(current_node.data)
            current_node = current_node.next


node1=Node(1)
node2=Node(2)
node1.next=node2

node3=Node(3)
node2.next=node3

list = LinkedList(node1)
#print(list.insert(3,5))
list.insert_at_index(2,10)
list.pr()
print()
list.delete_at_index(2)
list.pr()
print()
list.delete_at_beg()
list.pr()
print()
list.delete_at_end()
list.pr()

