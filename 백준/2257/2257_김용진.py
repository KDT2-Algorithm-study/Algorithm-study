# 화학식량
# 많은 시도를 해봤지만.. 결국 답지봄..
import sys
sys.stdin = open('input.txt','r')

word = input()
word_dict = {
    'H' : 1,
    'C' : 12,
    'O' : 16
}
stack = []
for i in word: 
    if i == '(':  # i 값에 (이 들어오면
        stack.append(i) # 스택에 ( append
    elif i == ')': # i 값에 )이 들어오면
        check = 0 # check = 0 이면서 while문 동작

        while 1:
            target = stack.pop() # 스택에 있는 제일 마지막 을 pop하고 그 값을 target에 저장
            if target == '(': # stact의 제일 마지막이 ( 이라면
                break # while문 종료
            check += target # check에 target값을 더해준다
        stack.append(check) # stack에 더한 check값을 append한다

    elif i in word_dict: # 해당 문자가 dict에 들어있다면
        stack.append(word_dict[i]) # 해당 딕셔너리의 value값을 stack로 append
    else:
        stack[-1] *= int(i) # 만약 숫자가 들어온다면 스택의 가장 마지막 수와 숫자와 곱해준다
print(sum(stack)) # 스택에 저장된 숫자를 다 더해준다

# from collections import deque
# import sys
# sys.stdin = open('input.txt','r')

# word = input()
# word_dict = {
#     'H' : 1,
#     'C' : 12,
#     'O' : 16
# }
# a = deque()
# b = []
# cnt1 = 0
# cnt2 = 0
# for i in word:
#     a.append(i)
# for key,value in word_dict.items():   
#     for x in range(len(a)):
#         if a[0] == key:
#             a.append(value)
#             a.popleft()
#         else:
#             a.append(a[0])
#             a.popleft()

# print(a)


# for q in range(len(a)):
#     cnt1 += a[q]
#     if '(' == a[q]:


    


    



# for key,value in word_dict.items():
#     for x in a:
#      temp = word.replace
#     if key in word:
#         word = word.replace(key,value)

# print(word)

# a = []
# b = []
# c = []
# d = []
# f = []
# word = input()
# word_dict = {
#     'H' : 1,
#     'C' : 12,
#     'O' : 16
# }

# for i in word:
#     if '(' == i:
#         b.append(i)
#     elif ')' == i:
#         b.append(i)
#     else:
#         a.append(i)
# # c.append(''.join(a))


# for x in a:
#     try:
#         c.append(int(x))
#     except:
#         c.append(x)

# print(c)
# for t in c:
#     if t not in word_dict:
#         word_dict[t] = t

# print(c)
# for key,value in word_dict.items():
#     for q in c:
#         if q in word_dict.keys:
#             print(q)
#         else:
#             print(q)





