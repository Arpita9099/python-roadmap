# Stock Market Buy Sell

class MaxSubArry:
    def __init__(self) -> None:
        pass

    def is_empty(self, arry):
        return len(arry) == 0
    
    def get_length(self, arry):
        return len(arry)
    
    def find_mid_index(self, arry):
        print(f"mid_index: {self.get_length(arry) // 2}")
        return (self.get_length(arry) // 2)
    
    def find_min_elm(self, arry):
        print(f"min_elm: {min(arry)}")
        return min(arry)

    def find_max_elm(self, arry):
        print(f"max_elm: {max(arry)}")
        return max(arry)
    
    def max_sub_arry(self, arry):
        if self.is_empty(arry) or self.get_length(arry) == 1:
            return 0
        
        if self.get_length(arry) == 2:
            print(f"two_length_output: {max(arry[1] - arry[0], 0)}")
            return max(arry[1] - arry[0], 0)
        
        mid_index = self.find_mid_index(arry)
        print(f"mid_index: {mid_index}")
        left_sub_list = self.max_sub_arry(arry[:mid_index])
        print(f"left_sub_list: {left_sub_list}")
        right_sub_list = self.max_sub_arry(arry[mid_index:])
        print(f"right_sub_list: {right_sub_list}")
        min_from_left = self.find_min_elm(arry[:mid_index])
        print(f"min_from_left: {min_from_left}")
        max_from_right = self.find_max_elm(arry[mid_index:])
        print(f"max_from_right: {max_from_right}")

        t = max(left_sub_list, right_sub_list, max_from_right-min_from_left)
        print(f"t: {t}")
        return t


if __name__ == "__main__":
    ob = MaxSubArry()
    print(ob.max_sub_arry([100, -2, 5, 10, 11, -4, 15, 9, 18, -2, 21, -11]))
