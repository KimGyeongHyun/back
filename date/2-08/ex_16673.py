class Wine:

    def __init__(self, C, K, P):
        self.C = C
        self.K = K
        self.P = P
        self.total_wine = 0

    def calc_wine_number(self):
        for i in range(self.C):
            n = i+1
            self.total_wine += self.K * n + self.P * n * n

    def return_total_wine(self):
        return self.total_wine


if __name__ == "__main__":
    C, K, P = map(int, input().split())
    wine = Wine(C, K, P)
    wine.calc_wine_number()
    print(wine.return_total_wine())
