tc = int(input())

for i in range(tc):
	p, q = map(int, input().split())
	s1 = (1 - p) * q
	s2 = p * (1 - q) * q
	print(f'#{i + 1}', 'YES' if s1 < s2 else 'NO')
