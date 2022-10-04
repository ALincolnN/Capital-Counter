"""
The project is about a function that takes a user input consisting of preferably numbers, converts
    them to integer data type and checks for the mode in the list.
The final check is to check if the mode number occurs more than half the length of the input list and if so,
    it returns the respective indexes of the mode number else it returns a -1.
"""
from statistics import mode


def solution(b):
    z = b.split(',')

    y = [eval(i) for i in z]

    i = []

    for x in range(len(y)):
        if y[x] == mode(y):
            i.append(x)

    if len(i) > len(y)/2:
        return i
    else:
        return -1


# a = [3, 4, 3, 2, 3, -1, 3, 3]


a = input('Enter single digits(0-9) of your choice separated by commas: ')

print(solution(a))
