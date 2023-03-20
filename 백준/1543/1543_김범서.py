docs = input()
word = input()
ref = 0
cnt = 0

while ref <= (len(docs) - len(word)):
    if docs[ref: ref + len(word)] == word:
        cnt += 1
        ref += len(word)
    else:
        ref += 1

print(cnt)
