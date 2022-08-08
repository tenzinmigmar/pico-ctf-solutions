import string

with open('message.txt') as f:
    lines = f.read()

# complete alphanumeric list provided in message.txt
decrypt_alpha = list("ekszjtcmxoqudylfabgphnrviwEKSZJTCMXOQUDYLFABGPHNRVIW")
alpha = list(string.ascii_letters)

lines = list(lines)

for i, letter in enumerate(lines):
    if letter in decrypt_alpha:
        index = decrypt_alpha.index(letter)
        lines[i] = alpha[index]
lines = "".join(lines)

print(lines)


