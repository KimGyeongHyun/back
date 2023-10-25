from sys import stdin


def get_kth_number(n, k):
    div = 1     # 10 ** (n의 자릿수)
    exp = 1     # 자릿수에 따른 숫자 갯수 (2자리면 2, 3자리면 3 ... )

    while n//div != 0:  # div *= 10 연산 계속하여 n의 끝까지 갈 때까지 반복

        if 9 * div * exp < k:   # 찾아야 하는 k 가 현재 자릿수의 총 숫자 갯수보다 많으면
            k -= 9 * div * exp  # k 에서 현재 자릿수의 총 숫자만큼 뺄셈
            div *= 10
            exp += 1            # 자릿수 옮김

        else:   # k가 현재 자릿수의 총 숫자 갯수 안에 있다면 k번째 숫자를 찾아 리턴
            if (n - div + 1) * exp < k:     # k가 n 에서 최대 출력할 수 있는 숫자 개수를 초과했다면 탈출
                break

            th1 = (k-1) // exp + div    # k번째 자리에 있는 숫자는 무슨 숫자인지 (ex: 15, 385, 2934 ...)
            th2 = (k-1) % exp
            th2 = exp - th2 - 1         # th1 에서 몇번째 자리인지

            return th1//(10**th2) % 10  # 숫자 th1 에서 th2 번째 자릿수 반환

    return -1


if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())
    print(get_kth_number(n, k))
