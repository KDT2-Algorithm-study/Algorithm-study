x, y, w, h = list(map(int, input().split()))
lst = []
lst.append(x)
lst.append(y)
lst.append(w-x)
lst.append(h-y)
print(min(lst))