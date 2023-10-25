class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):

        temp_string = ""
        iterator = self.head

        while iterator is not None:
            temp_string += "{}\n".format(iterator.data)
            iterator = iterator.next

        return temp_string


if __name__ == "__main__":

    linked_list = LinkedList()

    repeat = int(input())

    for _ in range(repeat):
        a, b = map(int, input().split())
        linked_list.append(a + b)

    print(linked_list)