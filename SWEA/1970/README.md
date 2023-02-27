# [1970. 쉬운 거스름돈](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE&problemTitle=1970&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1)


- 시간 : 10개 테스트케이스를 합쳐서 C++의 경우 30초 / Java의 경우 30초 / Python의 경우 30초
- 메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내
<br><br>

우리나라 화폐 ‘원’은 금액이 높은 돈을 우선적으로 계산할 때 돈의 개수가 가장 최소가 된다.
<br><br>
S마켓에서 사용하는 돈의 종류는 다음과 같다.
<br>50,000 원
<br>10,000 원
<br>5,000 원
<br>1,000 원
<br>500 원
<br>100 원
<br>50 원
<br>10 원
<br><br>
S마켓에서 손님에게 거슬러 주어야 할 금액 N이 입력되면 돈의 최소 개수로 거슬러 주기 위하여 각 종류의 돈이 몇 개씩 필요한지 출력하라.


### [예제]

N이 32850일 경우,
50,000 원 : 0개
10,000 원 : 3개
5,000 원 : 0개
1,000 원 : 2개
500 원 : 1개
100 원 : 3개
50 원 : 1개
10 원 : 0개


### [제약 사항]

1. N은 10이상 1,000,000이하의 정수이다. (10 ≤ N ≤ 1,000,000)

2. N의 마지막 자릿수는 항상 0이다. (ex : 32850)


### [입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
<br><br>
각 테스트 케이스에는 N이 주어진다.


### [출력]

각 줄은 '#t'로 시작하고, 다음줄에 각 돈의 종류마다 필요한 개수를 빈칸을 사이에 두고 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)