n = int(input())
books = {}
for _ in range(n):
    word = input()
    if word in books:
        books[word] += 1
    else:
        books[word] = 1
books_lst = list(books.items())

books_lst = sorted(books_lst,key =lambda x : (-x[1],x[0]))
print(books_lst[0][0])