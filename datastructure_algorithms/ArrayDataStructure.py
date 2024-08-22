# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

exp = {
    "JAN" : 2200,
    "FEB" : 2350,
    "MAR" : 2600,
    "APR" : 2130,
    "MAY" : 2190
}

# 1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra was spent compared to jan:",exp["FEB"] - exp["JAN"]) # 150

# 2. Find out your total expense in first quarter (first three months) of the year
print("Expense for first quarter:",exp["JAN"] + exp["FEB"] + exp["MAR"]) # 7150

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", True if 2000 in exp.values() else False) # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp["JUN"] = 1980
print("Expenses at the end of June:",exp) # {'JAN': 2200, 'FEB': 2350, 'MAR': 2600, 'APR': 2130, 'MAY': 2190, 'JUN': 1980}

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp["APR"] = exp["APR"] - 200
print("Expenses after 200$ return in April:",exp) # {'JAN': 2200, 'FEB': 2350, 'MAR': 2600, 'APR': 1930, 'MAY': 2190, 'JUN': 1980}


# 2. You have a list of your favourite marvel super heros
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this list

heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
print(len(heros)) # 5

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros) # ['spider man', 'thor', 'hulk', 'iron man', 'captain america', 'black panther']

# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros) # ['spider man', 'thor', 'hulk', 'black panther', 'iron man', 'captain america']

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros) # ['spider man', 'doctor strange', 'black panther', 'iron man', 'captain america']

# 5. Sort the list in alphabetical order
heros.sort()
print(heros) # ['black panther', 'captain america', 'doctor strange', 'iron man', 'spider man']


# 3. Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max_number = int(input(f"provide max value:"))
odd_list = [ i for i in range(1,max_number) if i%2 != 0]
print(odd_list)