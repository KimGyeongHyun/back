if __name__ == "__main__":
    angle1 = int(input())
    angle2 = int(input())
    angle3 = int(input())

    if angle1 + angle2 + angle3 != 180:
        print("Error")
    elif angle1 == angle2 and angle1 == angle3:
        print("Equilateral")
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        print("Isosceles")
    else:
        print("Scalene")