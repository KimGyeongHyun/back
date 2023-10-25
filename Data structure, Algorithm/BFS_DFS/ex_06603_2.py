import sys

input = sys.stdin.readline

# 반복적으로 수행되는 6번의 반복문을 DFS 로 구현한다

# DFS 를 수행할 때 리스트 깊은 복사가 되지 않도록 주의해야 함
# 해당 메소드에서 일반 변수 다루듯 리스트를 다루면 깊은 복사가 되어 값이 중첩된다
# l : 총 로또 숫자, nl : 현재 뽑은 숫자, c : 현재 뽑은 숫자 개수, index : 다음에 뽑을 공 인덱스

def num_pick(l, nl, c, index):

    if c == 6:  # 6개를 뽑았다면
        print(*nl)  # 뽑은 숫자 출력
        return  # 종료

    # 뽑은 숫자가 없을 경우 총 로또 숫자에서 뒤의 숫자 5개를 제외한 숫자를 모두 순회한다
    if c == 0:
        for i in range(len(l)-5):
            num_pick(l, [l[i]], c+1, i)
    else:   # 뽑은 숫자가 있을 경우
        # 뒤에 숫자의 "5개 - 뽑은 숫자 개수" 만큼을 제외하고 모두 순회한다
        for i in range(index+1, len(l)-5+c):
            tl = nl[:]  # 얕은 복사
            tl.append(l[i])     # 숫자 뽑기
            num_pick(l, tl, c+1, i)

if __name__ == "__main__":

    while True:
        l = list(map(int, input().split()))

        if l[0] == 0:
            break

        num_pick(l[1:], [], 0, 0)
        print()
