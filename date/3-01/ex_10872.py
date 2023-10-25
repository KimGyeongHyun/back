from sys import stdin

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i

    return result

if __name__ == "__main__":
    n = int(stdin.readline())

    print(factorial(n))