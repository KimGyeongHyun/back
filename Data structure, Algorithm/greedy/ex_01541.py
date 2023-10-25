from sys import stdin
import re

# -가 나오는 순간 뒤에 있는 모든 수는 괄호를 사용하여 -로 바꿀 수 있다
# 즉 합의 최소값을 구하기 위해선 -가 나오기 전까진 수를 더하고 - 이후로 수를 빼면 된다

if __name__ == "__main__":

    input_str = stdin.readline().strip()

    nl = list(map(int, re.split('[^0-9]', input_str)))
    cl = re.findall(r'[+-]', input_str)

    flag = False
    sum = nl[0]

    for i in range(len(nl)-1):
        if cl[i] == '-':
            flag = True
        if flag:
            sum -= nl[i+1]
        else:
            sum += nl[i+1]

    print(sum)
