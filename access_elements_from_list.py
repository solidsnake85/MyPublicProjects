# Write a program to access the 2nd, 4th and 5th elements from the list below:

raw_list = [1, ", a", 2, ", b", 3, " c"]


def dissect(list, x, y, z):
    elements = (x - 1, y - 1, z - 1)
    for i in elements:
        print(list[i])


dissect(raw_list, 2, 4, 5)

# my program allows to dissect any element
# leaves conversion of elements to computer
