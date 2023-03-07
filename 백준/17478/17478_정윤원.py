'''
N = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

def lagoloop(N) :
    global cnt

    def prcnt() :
        for i in range(cnt) :
            print("____", end="")    
        return None
    
    prcnt()
    print("\"재귀함수가 뭔가요?\"")
    
    if cnt != N :
        prcnt()
        print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        prcnt()
        print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        prcnt()
        print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        cnt += 1
        lagoloop(N)
    else :
        prcnt()
        print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")

        for i in range(N, -1, -1) :
            prcnt()
            print("라고 답변하였지.")
            cnt -= 1
    
    return None

cnt = 0
lagoloop(N)
'''
# 수정 (소현섭님 코드 많이 참조)

N = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

def lagoloop(n) :
    
    print(f"{'____'*(N-n)}\"재귀함수가 뭔가요?\"")
    
    if 0 != n :
        print(f"{'____'*(N-n)}\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        print(f"{'____'*(N-n)}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print(f"{'____'*(N-n)}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        lagoloop(n-1)
    else :
        print(f"{'____'*(N-n)}\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    
    print(f"{'____'*(N-n)}라고 답변하였지.")
    
    return None

lagoloop(N)