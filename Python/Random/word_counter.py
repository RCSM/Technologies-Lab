# Problems to be solved :
#   1. Get the text from the source
#   2. Read/Open it(if can't, check char set)
#   3. Close the file and end the script

stc = "How are you doing today. Hopefully you are doing great"

book = stc.split()
ctr = {}

for word in book:
    if word in ctr:#if ctr.has_key(word)
        ctr[word] = ctr[word]+1
    else:
        ctr[word] = 1

for key, value in ctr.items():
    print key, "appears", value, "time(s)"

# D : Get each letter
#for letter in stc:
#    print(letter)

# D : Get the words
#print(stc.split())