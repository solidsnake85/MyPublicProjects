# Write a program to print out the 2 table (up to 20) using a while loop


def table(n):
    i = 1
    while i <= 20:
        print(n, "*", i, "=", n * i)
        i = i + 1


table(2)

# My program allows for any int as argument for table
