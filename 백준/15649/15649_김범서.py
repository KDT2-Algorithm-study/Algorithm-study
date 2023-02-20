def chk():
    # 배열 안에 m개의 숫자가 있으면 출력하고 종료
    if len(number) == m:
        print(*number)
        return
    # 배열 안의 숫자가 m개가 아닐 때
    for i in range(n):
        if not visited[i]:
            # 방문처리 후 숫자 추가
            visited[i] = True
            number.append(i + 1)
            # 재귀호출
            chk()
            # 숫자를 pop한 후 방문처리를 취소한다
            number.pop()
            visited[i] = False


n, m = map(int, input().split())
number = list()
visited = [False for i in range(n)]

chk()
