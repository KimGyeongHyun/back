from sys import stdin

if __name__ == "__main__":

    for line in stdin:
        a, b = map(int, line.split())
        print(a + b)