# write a program to display the even numbers from 1 - 20 and how many there are
count = 0
for number in range(1, 20):
    if number % 2 == 0: # if remainder of number/2 = 0
        count += 1  # increments the count
        print(number)
print(f"There are {count} even numbers")