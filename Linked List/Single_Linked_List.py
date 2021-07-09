class Node:
    
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    Returns the number of nodes in the list takes O(n) time
    """

    def __init__(self):
        self.head = None

    def __repr__(self):

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '-> '.join(nodes)
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        
        current = self.head
        count = 0

        while current:
            count+=1
            current = current.next_node
            
        return count

    def add(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self,key):
        current = self.head

        while current:
            if current.data == key:
                return True
            current=current.next_node
            
        return None

    def insert(self,data,index):
        if index > self.size():
            print("insertion is not allow")
            return None
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head
            
            while position > 1:
                current = current.next_node
                position -= 1

            new.next_node  = current.next_node  # new.next_node = pre
            current.next_node =  new            # current.next_node = new
        
    def remove(self, key):
        
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
                
        return current
            
        


if __name__ == "__main__":
    LinkedList = LinkedList()
    LinkedList.add(10)
    LinkedList.add(20)
    LinkedList.add(30)
    LinkedList.add(60)
    LinkedList.remove(30)
    LinkedList.insert(40,2)
    LinkedList.insert(50,6)
    print(LinkedList.search(10))
    print(LinkedList.search(50))
    print(LinkedList)

        
