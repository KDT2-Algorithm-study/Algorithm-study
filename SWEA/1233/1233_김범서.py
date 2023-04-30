for i in range(1, 11):
	n = int(input())
	flag = False
	
	for j in range(n):
		chk = input().split()
		if len(chk) == 4:
			if chk[1].isdigit(): flag = True
			if not (chk[2].isdigit() and chk[3].isdigit()): flag = True
		elif len(chk) == 2:
			if not chk[1].isdigit(): flag = True

	print(f'#{i} 0' if flag else f'#{i} 1')
