import sys
from collections import defaultdict, Counter

n = int(sys.stdin.readline())
book = [sys.stdin.readline().rstrip() for _ in range(n)]

book = sorted(book)
book_dict = defaultdict(int)

for i in book:
    book_dict[i] += 1

print(Counter.most_common(book_dict, 1)[0][0])