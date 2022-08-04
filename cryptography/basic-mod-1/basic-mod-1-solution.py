import string

with open('message.txt') as f:
    lines = f.readlines()

# creating list of nums from message.txt
nums = [int(num) for num in lines[0].split()]

# function to find mod
def find_mod(a, m):
    mod = a % m
    return mod

# finding mod on nums
inv = []
for number in nums:
    inv.append(find_mod(number, 37))

new_string = ""
decimals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# mapping to appropriate chars
for val in inv:
    if val < 26:
        new_string += string.ascii_uppercase[val]
    elif 26 <= val < 36:
        new_string += str(decimals[val - 26])
    elif val == 36:
        new_string += "_"

print(new_string)