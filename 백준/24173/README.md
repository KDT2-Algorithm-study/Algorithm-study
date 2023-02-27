# [알고리즘 수업 - 힙 정렬 1](https://www.acmicpc.net/problem/24173)
 
|시간 제한	|메모리 제한	|제출	|정답	|맞힌 사람	|정답 비율|
|---|---|---|---|---|---|
|1 초	|512 MB	|228	|78	|51	|34.000%|

### 문제
오늘도 서준이는 최소 힙 기반 힙 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
<br><br>
N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 힙 정렬로 배열 A를 정렬할 경우 배열 A에 K 번째 교환되는 수를 구해서 우리 서준이를 도와주자.
<br><br>
크기가 N인 배열에 대한 힙 정렬 의사 코드는 다음과 같다.

```c++
heap_sort(A[1..n]) { # A[1..n]을 정렬한다.
    build_min_heap(A, n);
    for i <- n downto 2 {
        A[1] <-> A[i];  # 원소 교환
        heapify(A, 1, i - 1);
    }
}

build_min_heap(A[], n) {
    for i <- ⌊n / 2⌋ downto 1
        heapify(A, i, n)
}

# A[k]를 루트로 하는 트리를 최소 힙 성질을 만족하도록 수정한다.
# A[k]의 두 자식을 루트로 하는 서브 트리는 최소 힙 성질을 만족하고 있다.
# n은 배열 A의 전체 크기이며 최대 인덱스를 나타낸다.

heapify(A[], k, n) {
    left <- 2k; right <- 2k + 1;
    if (right ≤ n) then {
        if (A[left] < A[right]) then smaller <- left;
                                else smaller <- right;
    }
    else if (left ≤ n) then smaller <- left;
    else return;

    # 최소 힙 성질을 만족하지 못하는 경우 재귀적으로 수정한다.
    if (A[smaller] < A[k]) then {
        A[k] <-> A[smaller];
        heapify(A, smaller, n);
    }
}
```

### 입력
첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 500,000), 교환 횟수 K(1 ≤ K ≤ 108)가 주어진다.
<br>
다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

### 출력
K 번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력한다. 교환 횟수가 K 보다 작으면 -1을 출력한다.