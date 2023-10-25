from sys import stdin
import array as arr


if __name__ == "__main__":
    x, y = map(int, stdin.readline().split())
    days = arr.array('i', [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    seven = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    sum = 0
    for month in range(x-1):
        sum += days[month]

    sum += y - 1
    print(seven[sum % 7])