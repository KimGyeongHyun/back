if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(int(a*b/c) if b > c else int(a*c/b))