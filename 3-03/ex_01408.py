from sys import stdin


class Time:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def sub_time(self, time):
        self.hour -= time.hour
        self.minute -= time.minute
        self.second -= time.second
        self.set_time()

    def set_time(self):
        self.minute += self.second // 60
        self.second %= 60

        self.hour += self.minute // 60
        self.minute %= 60

        self.hour %= 24

    def print_time(self):
        print("{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second))


if __name__ == "__main__":
    a, b, c = map(int, stdin.readline().split(':'))
    curr_time = Time(a, b, c)
    a, b, c = map(int, stdin.readline().split(':'))
    start_time = Time(a, b, c)

    start_time.sub_time(curr_time)
    start_time.print_time()