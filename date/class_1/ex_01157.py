from sys import stdin
import array as arr

if __name__ == "__main__":

    a = arr.array('i', [0 for _ in range(26)])
    s = str(stdin.readline())

    s = s.lower()

    for char in s[:-1]:
        a[ord(char) % 97] += 1

    index = 0
    max = 0

    dup_flag = False
    for i in range(26):
        if max < a[i]:
            max = a[i]
            index = i
            dup_flag = False
        elif max == a[i]:
            dup_flag = True

    if dup_flag:
        print('?')
    else:
        print(chr(65 + index))
