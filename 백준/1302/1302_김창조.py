# 1302. 베스트셀러

import sys
input = sys.stdin.readline

N = int(input())
books = dict()

for _ in range(N):
    book = input().strip()
    books[book] = books.get(book, 0) + 1

books = sorted(books.items(), key=lambda x: (-x[1], x[0]))

print(books[0][0])