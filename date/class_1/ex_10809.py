from sys import stdin

if __name__ == "__main__":
    s = str(stdin.readline())
    char_int = 97
    for _ in range(26):
        print(s.find(chr(char_int)), end=' ')
        char_int += 1

