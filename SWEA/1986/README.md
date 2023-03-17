# [1986. 지그재그 숫자 D2](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PxmBqAe8DFAUq&categoryId=AV5PxmBqAe8DFAUq&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1)

- 시간 : 10개 테스트케이스를 합쳐서 C++의 경우 30초 / Java의 경우 30초 / Python의 경우 30초
- 메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.


### [예제 풀이]

N이 5일 경우,
<br>
1 – 2 + 3 – 4 + 5 = 3
<br>
N이 6일 경우,
<br>
1 – 2 + 3 – 4 + 5 – 6 = -3


### [제약사항]

N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


### [입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
<br>
각 테스트 케이스에는 N이 주어진다.


### [출력]

각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 누적된 값을 출력한다.
<br>
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)