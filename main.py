class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
        
class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def createDLL(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        new_node.next=new_node
        new_node.prev=new_node
        self.length+=1
        return "CDLL created"

    def insert(self,index,value):
        if self.head is None:
            return "CDLL Does not exist"
        if index < 0 or index > self.length:
            return "Index out of bounds"
        new_node=Node(value)
        if index==0:
            new_node.next=self.head
            new_node.prev=self.tail
            self.head.prev=new_node
            self.head=new_node
            self.tail.next=new_node
        elif index==self.length:
            new_node.prev=self.tail
            new_node.next=self.head
            self.head.prev=new_node
            self.tail.next=new_node
            self.tail=new_node
        else:
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            new_node.prev=temp_node
            new_node.next.prev=new_node
            temp_node.next=new_node
        self.length += 1
        return "Successfully added a node"
    
    def traversal(self):
        current=self.head
        while current:
            print(current.value)
            if current == self.tail:
                break
            current=current.next
            
    def reverseTraversal(self):
        current=self.tail
        while current:
            print(current.value)
            if current==self.head:
                break
            current=current.prev
            
    
cd_linked_list=CircularDoublyLinkedList()
cd_linked_list.createDLL(10)
print([node.value for node in cd_linked_list])
cd_linked_list.insert(1,40)
cd_linked_list.insert(0,70)
print([node.value for node in cd_linked_list])
cd_linked_list.traversal()
cd_linked_list.reverseTraversal()