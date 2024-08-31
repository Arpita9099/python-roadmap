class MergeSort:
    def __init__(self):
        pass

    def find_mid_index(self, arry):
        print(f"mid_index: {len(arry) // 2}")
        return len(arry) // 2
    
    def is_empty(self, arry):
        return len(arry) == 0
    
    def get_length(self, arry):
        print(f"len: {len(arry)}")
        return len(arry)
    
    def merge_two_sorted_list(self, left_sorted_list, right_sorted_list):
        sorted_list = []
        i = j = 0
        while left_sorted_list and right_sorted_list and i < len(left_sorted_list) and j < len(right_sorted_list):
                if left_sorted_list[i] <= right_sorted_list[j]:
                    sorted_list.append(left_sorted_list[i])
                    i += 1
                else:
                    sorted_list.append(right_sorted_list[j])
                    j += 1
        while left_sorted_list and i < len(left_sorted_list):
            sorted_list.append(left_sorted_list[i])
            i += 1
        while right_sorted_list and j < len(right_sorted_list):
            sorted_list.append(right_sorted_list[j])
            j += 1
        print(f"sorted_list: {sorted_list}")
        return sorted_list

    def merge_sort(self, arry):      
        if self.is_empty(arry):
            return arry
        
        if self.get_length(arry) == 1:
            return arry

        mid_index = self.find_mid_index(arry)
        left_sub_list = self.merge_sort(arry[:mid_index])
        print(f"left_sub_list: {left_sub_list}")
        right_sub_list = self.merge_sort(arry[mid_index:])
        print(f"right_sub_list: {right_sub_list}")
        t = self.merge_two_sorted_list(left_sub_list, right_sub_list)
        print(f"t : {t}")
        return t          
            
if __name__ == "__main__":
    ob = MergeSort()
    print(ob.merge_sort([1,4,6,2,3,8,7]))