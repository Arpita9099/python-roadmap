# input = "a1b23c456d"
# output = 786

import string

input_str = input("Provide List of Characters and Digits: ")
total_sum = 0
current_number = ''

for char in input_str:
    if char.isdigit():
        current_number += char  # Append digit characters to current_number
    else:
        if current_number:
            total_sum += int(current_number)  # Convert current_number to int and add to total_sum
            current_number = ''  # Reset current_number

# Add the last accumulated number to total_sum if not empty
if current_number:
    total_sum += int(current_number)

print("Total sum of consecutive digits:", total_sum)
