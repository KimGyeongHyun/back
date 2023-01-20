if __name__ == "__main__":

    seperator = "-----------------------"

    temp_string = '{:<15}{:<3}{:>2}{:>3}'
    print(temp_string.format('NFC West', 'W', 'L', 'T'))
    print(seperator)
    print(temp_string.format('Seattle', '13', '3', '0'))
    print(temp_string.format('San Francisco', '12', '4', '0'))
    print(temp_string.format('Arizona', '10', '6', '0'))
    print(temp_string.format('St. Louis', '7', '9', '0'))
    print()

    print(temp_string.format('NFC North', 'W', 'L', 'T'))
    print(seperator)
    print(temp_string.format('Green Bay', '8', '7', '1'))
    print(temp_string.format('Chicago', '8', '8', '0'))
    print(temp_string.format('Detroit', '7', '9', '0'))
    print(temp_string.format('Minnesota', '5', '10', '1'))
