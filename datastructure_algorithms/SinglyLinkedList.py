# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class SignlyLinkedList:
#     def __init__(self, head=None):
#         self.head = head

# if __name__ == '__main__':
#     ll = SignlyLinkedList()


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SignlyLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head == None:
            print("Linklist is empty.")
            return
   
        itr = self.head
        linklist_string = ''
        while itr != None:
            linklist_string = linklist_string + str(itr.data) + "-->"
            itr = itr.next
        print(linklist_string)

    def get_length(self):
        len = 0
        itr = self.head
        while itr != None:
            len = len + 1
            itr = itr.next
        return len

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            self.insert_at_begining(data)
            return
        
        itr = self.head
        while itr.next != None:
            itr = itr.next

        node = Node(data, None) 
        itr.next = node

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
            return 

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count + 1

    def remove_at(self, index):

        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return 
        
        count = 0
        itr = self.head
        while itr != None:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count = count + 1

    def insert_values(self, data_list):
        for elm in data_list:
            self.insert_at_end(elm)
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            return
        
        itr = self.head
        while itr!= None:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next 

    def remove_by_value(self, data):
        if self.head == None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next != None:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
        else: # execute only if while loop finished without bracking
            print(f"{data} not in list.")


if __name__ == '__main__':
    ll = SignlyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print() # banana-->mango-->grapes-->orange-->
    ll.insert_after_value("mango","apple")
    ll.print() # banana-->mango-->apple-->grapes-->orange-->
    ll.remove_by_value("orange")
    ll.print() # banana-->mango-->apple-->grapes-->
    ll.remove_by_value("figs") # figs not in list.
    ll.print() # banana-->mango-->apple-->grapes-->
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.print() # grapes-->
    ll.remove_by_value("grapes")
    ll.print() # Linklist is empty.
    print(f"length:",ll.get_length()) # length: 0
    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print() # 45-->7-->12-->567-->99-->67-->