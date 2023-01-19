if __name__ == "__main__":
    a, b = map(int, input().split())

    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('==')