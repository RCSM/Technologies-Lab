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
