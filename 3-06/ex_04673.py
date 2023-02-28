def guess_cr(a):
    """1의 자릿수를 제외한 수를 받음, 1의 자릿수의 숫자를 0으로 가정하고 생성자 추측하여 리턴"""
    sum_a = 0
    index = len(str(a))
    while 0 <= index:
        sum_a += (a//(10**index))%10
        index -= 1

    return 10 * a + sum_a


def is_not_self(n):
    """샐프 넘버가 아니면 True, 맞으면 False 리턴"""

    # 2의 자릿수 이상으로만 추측한 생성자에서 1의 자릿수가 0 ~ 9 까지의 생성자가 자동으로 도출됨
    # 추측한 생성자 = (2의 자릿수로 이상으로만 추측한 생성자 + 1의 자릿수 * 2)
    # 즉 2의 자릿수 이상으로만 추측한 생성자에서 나머지 1의 자릿수 경우의 수 10개를 한꺼번에 도출할 수 있음
    # 따라서 2의 자릿수 이상으로만 생성자를 우선 추측

    index = n//10   # 1의 자릿수를 제거한 수
    pre_cr = guess_cr(index)    # 2의 자릿수 이상으로만 추측한 생성자

    # 먼저 n의 2의 자릿수 이상으로만 추측한 생성자 비교
    # 처음 추측한 생성자는 n 보다 작을 수 없음
    # 만약 추측한 생성자의 1의자리 0~9 까지의 생성자 중 n 과 같은 생성자가 있다면 샐프 넘버 -> False 리턴
    # index 를 1 씩 빼가며 반복
    # 반복하다가 추측한 생성자가 n보다 너무 작아졌다면 생성자가 없다고 판단 -> True 리턴

    while pre_cr + 25 > n and 0 <= index:

        if pre_cr <= n <= pre_cr + 18 and (pre_cr - n) % 2 == 0:
            return False
        index -= 1
        pre_cr = guess_cr(index)

    return True


if __name__ == "__main__":
    for i in range(1, 10001):
        if is_not_self(i):
            print(i)