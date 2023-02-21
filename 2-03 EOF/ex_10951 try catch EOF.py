if __name__ == "__main__":

    while True:
        try:
            a, b = map(int, input().split())
        except EOFError as e:
            break
        print(a + b)
