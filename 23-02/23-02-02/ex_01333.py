if __name__ == "__main__":
    N, L, D = map(int, input().split())

    call_time = 0

    while True:

        if call_time >= N*L + (N-1)*5:
            print(call_time)
            quit()

        else:
            for i in range(N):
                temp_value = call_time - ((i+1)*L + i*5)
                if 0 <= temp_value <= 4:
                    print(call_time)
                    quit()
        call_time += D