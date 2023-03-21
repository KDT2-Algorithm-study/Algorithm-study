words = input()
search_word = input()
n = len(search_word)
cnt = 0

start = 0
end = n
while end <= len(words):
    if search_word == words[start:end]:
        cnt += 1
        start += n
        end += n
        
    else:
        start += 1
        end += 1
        
print(cnt)