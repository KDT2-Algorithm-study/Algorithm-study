book_dict = {}
for _ in range(int(input())):
    s = input()
    if s not in book_dict:
        book_dict[s] = 1
    else:
        book_dict[s] += 1

print(sorted(book_dict.items(), key=lambda x:(-x[1], x[0]), reverse=True)[-1][0])