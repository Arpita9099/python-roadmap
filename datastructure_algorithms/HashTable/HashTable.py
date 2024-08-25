# Implement hash table collision handling using linear probing

# class HashTable:
#     def __init__(self):
#         self.MAX = 10
#         self.arr = [[] for elm in range(self.MAX)]

# if __name__ == "__main__":
#     ob = HashTable()

class HashTable:
    def __init__(self):
        self.MAX = 3
        self.arr = [None for elm in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for ch in key:
            hash += ord(ch) # ord(ch) provide charector's asci value
        return (hash % self.MAX)
    
    def __setitem__(self, key, val): # def set_item(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] == None:
            self.arr[h] = (key,val)
        else:
            for index,elm in enumerate(self.arr[h+1:]):
                if elm == None:
                    self.arr[index] = (key,val)
                    break
            else:
                for index,elm in enumerate(self.arr[:h]):
                    if elm == None:
                        self.arr[index] = (key,val) 
                        break
                else: 
                    print(f"No Space Available for {key}")
                    
    def __getitem__(self, key): # get_item(self, key):
        h = self.get_hash(key)
        for item in self.arr:
            if item != None and item[0] == key:
                return item[1]
            
    def __delitem__(self, key): # delete_item(self, key):
        for index, elm in enumerate(self.arr):
            if elm != None and elm[0] == key:
                self.arr[index] = None
                break
        else:
            print(f"{key} is not present to delete.")

if __name__ == "__main__":
    ob = HashTable()
    ob["march 1"] = 11 # ob.set_item("march 1", 11)
    ob["march 2"] = 12
    ob["march 4"] = 14
    print(ob.arr)
    print(f"march 1: {ob['march 1']}") # print(f"march 1: {ob.get_item('march 1')}")
    del ob["march 4"] # ob.delete_item("march 4")
    print(ob.arr)
