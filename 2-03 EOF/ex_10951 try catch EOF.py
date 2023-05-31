if __name__ == "__main__":

    # EOF 의 경우 sys.stdin.readline() 이 먹히지 않는다
    # stdin 을 사용하고 싶으면 들어온 문자열이 ""인지 확인하고 예외처리하면 된다

    while True:
        try:
            a, b = map(int, input().split())
        except EOFError as e:
            break
        print(a + b)
