from sys import stdin


def is_palindrome(input_str):

    for i in range(len(input_str) // 2):
        if input_str[i] != input_str[len(input_str)-1-i]:
            return False

    return True


if __name__ == "__main__":

    while True:
        input_str = stdin.readline().strip()
        if input_str == "0":
            break
        if is_palindrome(input_str):
            print("yes")
        else:
            print("no")