if __name__ == "__main__":
    S, K, H = map(int, input().split())

    if S + K + H >= 100:
        print("OK")
    else:
        if S <= K and S <= H:
            print('Soongsil')
        elif K <= H:
            print('Korea')
        else:
            print('Hanyang')