import random


# 0 ~ 1 사이의 랜덤 실수
print(random.random())

# 2개의 숫자 사이 랜덤 실수
print(random.uniform(1, 2))

# 2개의 숫자 사이 랜덤 정수
print(random.randint(1, 10))

nm = []
l = []

for i in range(10):
    nm.append(random.randint(1, 5))
    print(nm[i], end=' ')

print()

for i in range(nm[0]):
    for j in range(nm[1]):
        print(random.randint(10, 99), end=' ')
    print()
