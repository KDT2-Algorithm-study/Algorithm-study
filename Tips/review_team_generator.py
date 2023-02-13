# Review Team generator

import sys
from random import shuffle
from pprint import pprint

sys.stdin = open("member_list.txt", encoding="UTF-8")

# 6회차_김창조
# 4회차_김신혜
# 5회차_정소담
# 4회차_김범서
# 5회차_박태양
# 6회차_노현석
# 4회차_박지환
# 5회차_소현섭
# 4회차_정윤원
# 6회차_김용진
# 4회차_장민지
# 5회차_이혜지

# 빠진 인원들 추가
del_lst = [
    "",
]

people_num = int(input())
people_lst = []
team_lst = [mem for _ in range(4) for mem in range(1, 4)]
# 발표자 지정
team_lst[0] = (1, "발표")
team_lst[1] = (2, "발표")
team_lst[2] = (3, "발표")

# 스터디원 people_lst에 추가
for _ in range(people_num):
    people_lst.append(input())

# 빠진 인원들 추첨 명단에서 제외
for mem in del_lst:
    people_lst.remove(mem)

# 빠진 인원수만큼 team_lst에서 제거
for i in range(len(del_lst)):
    team_lst.pop()

shuffle(team_lst)

print(*list(zip(people_lst, team_lst)), sep="\n")