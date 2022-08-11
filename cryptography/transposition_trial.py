with open('message (12).txt') as f:
    message = f.read()

# turn msg into list of 3 strings
block_msg = [message[i:i+3] for i in range(0, len(message), 3)]

# the first msg is 'heT' and should be 'The'
# to fix, move (referred to by index):
# index 0 -> index 1
# index 1 -> index 2
# index 2 -> index 0
unscrambled_msg = [msg[-1] + msg[:-1] for msg in block_msg]
final_msg = "".join(unscrambled_msg)

print(final_msg)
