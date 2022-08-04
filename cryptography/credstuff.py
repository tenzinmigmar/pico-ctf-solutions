import string
import codecs

with open('usernames.txt') as f:
    count = 0
    for i in f:
        count += 1
        if i.rstrip('\n') == "cultiris":
            print(count) # password is at line 378

with open('passwords.txt') as f:
    count = 0
    for i in f:
        count += 1
        if count == 378:
            password = i.rstrip('\n')

# to decrypt the password,
# explanation: the first 7 letters = picoCTF
# with this cipher, p = c, and S = F, which
# is the ROT13 substitution cypher.

print(codecs.encode(password, "rot_13"))

