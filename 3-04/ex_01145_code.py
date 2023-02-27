from sys import stdin


if __name__ == "__main__":
    a, b, c, d, e = map(int, stdin.readline().split())

    # num 을 1씩 증가시키며 적어도 3개 이상의 배수인지 확인한다
    num = 1
    while True:
        count = 0
        if num % a == 0: count += 1
        if num % b == 0: count += 1
        if num % c == 0: count += 1
        if num % d == 0: count += 1
        if num % e == 0: count += 1
        if count >= 3: break
        num += 1

    print(num)
