from collections import Counter
book = [input() for _ in range(int(input()))]
books = Counter(book)
cnt = max(books.values())
best = []

for k,v in books.items():
    if v == cnt:
        best.append(k)
print(sorted(best)[0])