if __name__ == "__main__":
    a, b = map(int, input().split())
    sub = a - b

    print(sub if sub >= 0 else -sub)