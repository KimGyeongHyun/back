from sys import stdin
import heapq

# 해당 풀이는 시간초과가 났다
# 최대 값 삭제 연산에서 힙 연산을 사용하지 않았으므로 시간복잡도가 올라갔기 때문으로 본다

if __name__ == "__main__":
    t = int(stdin.readline())
    for _ in range(t):  # 테스트 케이스 수 만큼 반복
        k = int(stdin.readline())
        lf = []     # 최소 힙

        for _ in range(k):  # 삽입, 삭제 연산

            str = stdin.readline().split()
            input_num = int(str[1])
            if str[0] == "I":   # 삽입 연산
                heapq.heappush(lf, input_num)

            elif str[0] == "D":     # 삭제 연산
                if input_num == 1:  # 최댓값 삭제
                    if not lf:  # 최소 힙에 요소가 없다면 삭제 연산을 수행할 수 없다
                        continue
                    idx = -1
                    val_max = -int(1e9)
                    for i in range(len(lf)):
                        if val_max <= lf[i]:
                            idx = i; val_max = lf[i]
                    del lf[idx]

                elif input_num == -1:   # 최소값 삭제
                    if not lf:  # 최소 힙에 요소가 없다면 삭제 연산을 수행할 수 없다
                        continue
                    num = heapq.heappop(lf)     # 최소 힙 삭제 연산

        # 결과 출력
        if not lf:
            print("EMPTY")
        else:
            print(max(lf), heapq.heappop(lf))