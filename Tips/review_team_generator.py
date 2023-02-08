# Review Team generator

import sys
from random import shuffle
from pprint import pprint

sys.stdin = open("member_list.txt", encoding="UTF-8")

people_num = int(input())
people_lst = []
team_lst = [[mem] for _ in range(4) for mem in range(1, 4)]

cnt_1 = 0
cnt_2 = 0
cnt_3 = 0

for _ in range(people_num):
    people_lst.append(input())
    
shuffle(team_lst)

print(*list(zip(people_lst, team_lst)), sep="\n\n")