from sys import stdin


# 3) 01654. 랜선 자르기 문제와 같은 형식으로 풀이
def get_tree_height_sum(input_list, input_cut_height):

    tree_height_sum = 0
    for tree_height in input_list:
        if tree_height > input_cut_height:
            tree_height_sum += tree_height - input_cut_height

    return tree_height_sum


if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    l = list(map(int, stdin.readline().split()))

    start = 0
    end = max(l)

    while True:

        mid = (start + end) // 2

        if mid == start:
            if get_tree_height_sum(l, mid+1) >= m:
                mid += 1
            break

        trees = get_tree_height_sum(l, mid)

        if trees >= m:
            start = mid
        else:
            end = mid

    print(mid)