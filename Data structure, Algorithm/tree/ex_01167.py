from sys import stdin

res = 0

# 1967번 문제 트리의 지름 풀이와 동일


def get_tree(start, end, weight):
    """간선으로부터 부모 -> 자식 의 방향성을 가진 트리 구성"""

    if visit[end]:
        return
    visit[end] = True
    g[start].append((end, weight))

    for e_end, e_weight in ig[end]:
        get_tree(end, e_end, e_weight)


def get_biggest_diameter(input_node):

    global res

    first, second = 0, 0

    for dest, w in g[input_node]:

        child_w = get_biggest_diameter(dest) + w

        if first < child_w:
            second = first
            first = child_w
        elif second < child_w:
            second = child_w

    if res < first + second:
        res = first + second

    return first


if __name__ == "__main__":
    v = int(stdin.readline())
    ig = [[] for _ in range(v+1)]
    g = [[] for _ in range(v+1)]
    visit = [False for _ in range(v+1)]

    for _ in range(v):
        l = list(map(int, stdin.readline().split()))
        node = l[0]
        for i in range(1, len(l)-2, 2):
            ig[node].append((l[i], l[i+1]))

    get_tree(0, 1, 0)

    get_biggest_diameter(1)
    print(res)

