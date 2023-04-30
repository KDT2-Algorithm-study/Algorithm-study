book = dict()
n = int(input())

for i in range(n):
	title = input()
	if title not in book:
		book[title] = 1
	else:
		book[title] += 1

maxnum = max(book.values())
result = list()

for key, value in book.items():
	if value == maxnum:
		result.append(key)

result.sort()
print(result[0])
