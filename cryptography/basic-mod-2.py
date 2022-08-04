import string

with open('message.txt') as f:
    lines = f.readlines()

# creating list of nums from message.txt
nums = [int(num) for num in lines[0].split()]

# function to find mod inv
def find_mod_inv(a,m):
    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            return x
    raise Exception('The modular inverse does not exist.')

# finding mod inv on nums
inv = []
for number in nums:
    inv.append(find_mod_inv(number, 41))

new_string = ""
decimals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# mapping to appropriate chars
for val in inv:
    # mapping for alphabet
    if 0 < val < 27:
        new_string += string.ascii_uppercase[val - 1]
    elif 27 <= val < 37:
        new_string += str(decimals[val - 27])
    elif val == 37:
        new_string += "_"

print(new_string)