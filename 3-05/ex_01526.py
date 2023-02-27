from sys import stdin


def gummin(n):
    index = len(str(n)) - 1     # 숫자 크기 인덱스
    res = 0
    while n > 0:

        # num : 제일 상위 숫자
        num = n // 10**index

        # 상위 숫자가 4, 7이 아니라면 예외 처리
        if num != 4 and num != 7:
            # 7 초과라면 해당 인덱스에 7을 채움
            if 7 < num:
                res += 7 * 10 ** index
            # 4 초과 7 미만이라면 해당 인덱스에 4를 채움
            elif 4 < num < 7:
                res += 4 * 10 ** index

            # 해당 인덱스-1 ~ 1의 자리까지 7을 채워 리턴
            index -= 1
            while index >= 0:
                res += 7 * 10**index
                index -= 1
            return res

        # 4 또는 7
        else:
            # 인덱스-1 숫자가 4 이상이라면 해당 인덱스에 num 을 넣는다
            # n의 상위 숫자를 빼고 index 를 1 뺀다
            # 인덱스-1 부터 반복한다 (while 문으로 돌아감)
            if 4 <= (n // 10**(index-1))%10:
                res += num * 10**index
                n -= num * 10**index
                index -= 1

            # 인덱스-1 숫자가 4 미만이면 예외 처리
            else:
                if num == 7:    # 인덱스 숫자가 7이라면 해당 인덱스에 4를 채움
                    res += 4 * 10 ** index

                # 1의 자리까지 7로 채우고 리턴
                index -= 1
                while index >= 0:
                    res += 7 * 10 ** index
                    index -= 1
                return res

    # 혹시 모를 예외 처리
    return res


if __name__ == "__main__":
    n = int(stdin.readline())
    print(gummin(n))