from sys import stdin


class Queue:

    def __init__(self):
        self.l = []

    def push(self, data: int):
        self.l.append(data)

    # 해당 연산은 오래 걸릴 수 있음
    # 큐를 정석적으로 구성한다면 l의 index 를 start, end 로 구성하고
    # l 의 전체 데이터를 앞으로 옮기는 대신 start, end 만 옮겨서 구성해야함
    # (10000 size 의 리스트 구성도 필요)
    def pop(self) -> int:
        if len(self.l) == 0:
            return -1
        else:
            return_int = self.l[0]
            self.l = self.l[1:]
            return return_int

    def size(self) -> int:
        return len(self.l)

    def empty(self) -> int:
        if len(self.l) == 0:
            return 1
        else:
            return 0

    def front(self) -> int:
        if len(self.l) == 0:
            return -1
        else:
            return self.l[0]

    def back(self) -> int:
        if len(self.l) == 0:
            return -1
        else:
            return self.l[-1]


if __name__ == "__main__":
    queue = Queue()

    n = int(stdin.readline())

    for _ in range(n):

        s = stdin.readline().strip()

        if len(s) >= 4 and s.split()[0] == "push":
            queue.push(int(s.split()[1]))

        if s == "pop":
            print(queue.pop())

        if s == "size":
            print(queue.size())

        if s == "empty":
            print(queue.empty())

        if s == "front":
            print(queue.front())

        if s == "back":
            print(queue.back())
