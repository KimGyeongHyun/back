from sys import stdin
import array as arr


if __name__ == "__main__":
    student_number, end_time = map(int, stdin.readline().split())
    student_time_gap_array = arr.array('i')

    for _ in range(student_number):
        student_time_gap_array.append(int(stdin.readline()))

    time_array = arr.array('i', [0 for _ in range(end_time + 1)])
    for student_time_gap in student_time_gap_array:
        for i in range(student_time_gap, end_time + 1, student_time_gap):
            time_array[i] = 1

    sum = 0
    for see in time_array:
        sum += see

    print(sum)
