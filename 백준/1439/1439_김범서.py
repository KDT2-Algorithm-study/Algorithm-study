s = input()
chk = [0, 0]

if s[0] == '0': chk[0] += 1
else: chk[1] += 1

for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        if s[i] == '0': chk[0] += 1
        else: chk[1] += 1

print(min(chk))
