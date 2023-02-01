if __name__ == "__main__":
    N = int(input())

    cute = 0

    for _ in range(N):
        vote = int(input())
        if vote == 1:
            cute += 1

    if cute > N//2:
        print('Junhee is cute!')
    else:
        print('Junhee is not cute!')