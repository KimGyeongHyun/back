from sys import stdin
import heapq
# from my_lib.tools import *

# 힙의 중간 요소를 제거하면 시간복잡도가 증가하기 때문에 다른 방식 사용

# 힙에서 삭제할 숫자를 따로 힙으로 구성
# 기존 힙과 우선순위가 같은 힙으로 '삭제할 요소가 들어있는 힙'을 구성하면
# 기존 힙에서 요소를 pop 해야할 때 '삭제할 요소가 들어있는 힙'과 비교하여 제외하면 된다
# 그러면 시간복잡도에 영향을 주지 않는다

# 기본 작동 방식
# 최소 힙, 최대 힙, 최소 힙에서 삭제할 숫자가 모여있는 최소 힙, 최대 힙에서 삭제할 숫자가 모여있는 최대 힙 구성
# 숫자가 추가될 때마다 최소 힙, 최대 힙에 추가
# 최대 값이 삭제될 때는 최대 힙 삭제, 해당 값을 삭제할 최소 힙에 추가
# 최소 값이 삭제될 때는 최소 힙 삭제, 해당 값을 삭제할 최대 힙에 추가
# 힙에서 숫자를 삭제할 때는 위에서 언급했듯이 '삭제할 숫자가 들어있는 힙'과 먼저 갱신을 한 다음 삭제한다


if __name__ == "__main__":
    t = int(stdin.readline())
    for _ in range(t):  # 테스트 케이스 수 만큼 반복
        k = int(stdin.readline())
        lf = []     # 최소 힙
        ls = []     # 최대 힙
        lfd = []    # 삭제할 숫자가 들어있는 최소 힙
        lsd = []    # 삭제할 숫자가 들어있는 최대 힙

        for _ in range(k):  # 삽입, 삭제 연산

            str = stdin.readline().split()
            input_num = int(str[1])
            if str[0] == "I":   # 삽입 연산
                heapq.heappush(lf, input_num)
                heapq.heappush(ls, -input_num)

            elif str[0] == "D":     # 삭제 연산
                if input_num == 1:  # 최댓값 삭제
                    while lsd and ls[0] == lsd[0]:  # 우선 최대 힙을 '삭제할 숫자가 들어있는 최대 힙'에 따라 갱신한다
                        heapq.heappop(ls)
                        heapq.heappop(lsd)
                    if not ls:  # 최대 힙에 요소가 없다면 삭제 연산을 수행할 수 없다
                        continue
                    num = heapq.heappop(ls)     # 최대 힙 삭제 연산
                    heapq.heappush(lfd, -num)   # '삭제할 숫자가 들어있는 최소 힙'에 해당 숫자 추가

                elif input_num == -1:   # 최소값 삭제
                    while lfd and lf[0] == lfd[0]:  # 우선 최소 힙을 '삭제할 숫자가 들어있는 최소 힙'에 따라 갱신한다
                        heapq.heappop(lf)
                        heapq.heappop(lfd)
                    if not lf:  # 최소 힙에 요소가 없다면 삭제 연산을 수행할 수 없다
                        continue
                    num = heapq.heappop(lf)     # 최소 힙 삭제 연산
                    heapq.heappush(lsd, -num)   # '삭제할 숫자가 들어있는 최대 힙'에 숫자 추가

        # 모든 연산을 마치고 힙에서 삭제할 숫자를 갱신한다
        while lsd and ls[0] == lsd[0]:
            heapq.heappop(ls)
            heapq.heappop(lsd)
        while lfd and lf[0] == lfd[0]:
            heapq.heappop(lf)
            heapq.heappop(lfd)

        # 결과 출력
        if not ls:
            print("EMPTY")
        else:
            print(-heapq.heappop(ls), heapq.heappop(lf))