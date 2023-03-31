import sys
input = sys.stdin.readline

# get_div(나뉠 수, 거듭 제곱할 수, 나눌 수) -> 나머지 리턴
# 해당 메소드에서 바뀌는 파라미터는 거듭 제곱할 수 뿐이다

# get_div(a, b, c) * get_div(d, b, c) % c = get_div(a*d, b, c) 증명
# a = f * c + g, b = h * c + i 라면
# get_div(a, b, c) = g
# get_div(d, b, c) = i
# get_div(a, b, c) * get_div(d, b, c) = g * i
# get_div(a*d, b, c) = ((f * h * c + g * h + i * f) * c + g * i) % c = (g * i) % c

# 위의 조건을 활용, 함수를 재귀적으로 구성할 수 있다
# (앞으로 get_div 안의 파라미터는 거듭 제곱할 수만 표현하겠습니다)  /   (get_div(거듭 제곱할 수))
# c : 나눌 수
# get_div(1) 은 바로 나온다
# get_div(2) = (get_div(1) * get_div(1)) % c
# get_div(3) = (get_div(2) * get_div(1)) % c
# get_div(n) = (get_div(n//2) * get_div(n - n//2)) % c

# 재귀 함수로 구성하더라도 거듭 제곱할 수가 매우 크면 연산량이 많아질 수 있다
# 특히 get_div(r) 중 r이 낮은 경우는 재귀적으로 볼 때 많이 불리게 된다
# 따라서 r 값에 따른 get_div 결과값을 딕셔너리에 저장하여
# key : r -> value : get_dic(get_div(r)) 의 형태로 저장한다
# r값이 딕셔너리에 있으면 값을 가져오고, 없으면 딕셔너리에 갱신한다
# 정답이 나올 때까지 해당 연산을 반복한다

div_dict = {}


def get_div(n, recurr, div):

    # 거듭 제곱할 수가 1이라면 해당 값을 리턴
    if recurr == 1:
        return n % div

    # 딕셔너리에 해당 연산을 이미 했을 경우 값을 가져와 리턴
    if recurr in div_dict.keys():
        return div_dict[recurr]

    # 반으로 나눠 재귀 호출
    one = get_div(n, recurr // 2, div)
    two = get_div(n, recurr - (recurr // 2), div)
    value = one * two % div
    # 해당 연산을 딕셔너리에 갱신
    div_dict[recurr] = value
    return value


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(get_div(a, b, c))