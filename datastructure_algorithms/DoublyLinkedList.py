# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev 


# class DoublyLinkedList:
#     def __init__(self, head=None):
#         self.head = head


# if __name__ == '__main__':
#     ll = DoublyLinkedList()


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev 


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    # def is_empty(self):
    #     if self.head == None:
    #         return True
    #     else:
    #         return False
    
    def is_empty(self):
        return self.head == None
    
    def create_node(self, data, next, prev):
        return Node(data, next, prev)

    def get_last_node(self):
        if self.is_empty():
            return
        itr = self.head
        while itr.next != None:
            itr = itr.next
        last_node = itr
        return last_node
    
    def get_length(self):
        if self.is_empty():
            return 0
        
        count = 0
        itr = self.head
        while itr != None:
            itr = itr.next
            count = count + 1
        return count
            
    def insert_at_begining(self, data):
        node = self.create_node(data, self.head, None)
        if self.is_empty():
            self.head = node
        else:
            self.head.prev = node
            self.head = node

    def insert_at_end(self,data):
        itr = self.get_last_node()
        node = self.create_node(data, None, itr)
        if self.is_empty():
            self.head = node
        else:
            itr.next = node

    def insert_at(self, index, data):
        if index <0 or index >= self.get_length():
            itr = self.head
            count = 0
            while itr != None:
                if count == index - 1:
                    node = self.create_node(data, itr.next, itr)
                    if node.next != None:
                        node.next.prev = node
                    itr.next = node
                    break
                itr = itr.next
                count += 1

    def remove_at(self, index):
        if index <0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next

        itr = self.head
        count = 0
        while itr != None:
            if count == index - 1:
                if itr.next.next != None:
                    itr.next = itr.next.next
                else:
                    itr.next = None
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        for elm in data_list:
            self.insert_at_end(elm)

    def print_forward(self):        
        if self.is_empty():
            print("Emplty List.")
            return
        
        itr = self.head
        linklist_string = ''
        while itr != None:
            linklist_string = linklist_string + str(itr.data) + '-->'
            itr = itr.next
        print(f"forward:{linklist_string}")

    def print_backward(self):        
        if self.is_empty():
            print("Emplty List.")
            return
        
        itr = self.get_last_node()
        linklist_string = ''
        while itr != None:
            linklist_string = linklist_string + str(itr.data) + '-->'
            itr = itr.prev
        print(f"Backward: {linklist_string}")


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(4)
    ll.print_forward() # forward:4-->5-->
    ll.print_backward() # Backward: 5-->4-->
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.print_forward() # forward:4-->5-->1-->2-->
    print(f"length:",ll.get_length()) # length: 4
    ll.remove_at(2)
    ll.print_forward() # forward:4-->5-->2-->
    ll.insert_values(["a","b","c"])
    ll.print_forward() # forward:4-->5-->2-->a-->b-->c-->