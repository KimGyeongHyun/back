from sys import stdin


def get_guess_width(x, y, c):

    # width 를 유추해 c를 계산
    # 계산한 c와 파라미터 c를 비교하여 이분법으로 width 를 다시 설정
    # 계산한 c가 파라미터 c의 특정 범위 내에 들어갔다면 width 리턴

    # width 의 max 값은 x, y 를 넘을 수 없음
    # 즉 x, y중 작은 값을 max 로 설정
    if x < y:
        max = x
    else:
        max = y

    # max와 min 사이값을 width 로 설정
    width = max/2
    min = 0

    while True:

        # width 로 guess_c 를 구함
        left = (x ** 2 - width ** 2) ** (1 / 2)
        right = (y ** 2 - width ** 2) ** (1 / 2)
        guess_c = left * right / (left + right)

        # c와 유사하다면 리턴
        if -0.0005 <= guess_c - c <= 0.0005:
            return width

        # c와 값이 차이가 난다면 max or min 값을 이분법으로 조정해 다시 width 를 설정
        if guess_c < c:
            max -= (max - min) / 2
        else:
            min += (max - min) / 2

        width = (min + max) / 2


if __name__ == "__main__":
    x, y, c = map(float, stdin.readline().split())
    print(get_guess_width(x, y, c))