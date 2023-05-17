import random


# # 0 ~ 1 사이의 랜덤 실수
# print(random.random())
#
# # 2개의 숫자 사이 랜덤 실수
# print(random.uniform(1, 2))
#
# # 2개의 숫자 사이 랜덤 정수
# print(random.randint(1, 10))
#
# nm = []
# l = []
#
# for i in range(10):
#     nm.append(random.randint(1, 5))
#     print(nm[i], end=' ')
#
# print()
#
# for i in range(nm[0]):
#     for j in range(nm[1]):
#         print(random.randint(10, 99), end=' ')
#     print()

MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_SUM = 365

def get_month_day(days):
    month = 1
    while days > 0:
        days -= MONTH_DAYS[month]
        month += 1

    return month-1, days + MONTH_DAYS[month-1]

print(15)
for i in range(15):
    x = random.randint(1, 365)
    y = random.randint(x, 365)
    xm, xd = get_month_day(x)
    ym, yd = get_month_day(y)
    print(xm, xd, ym, yd)