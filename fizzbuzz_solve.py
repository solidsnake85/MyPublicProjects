# fizz_buzz algorithm - solve it
# fizz_buzz takes input, depending on the input I give it, returns different results.
# rules:
# 1. If input given is divisible by 3, it will return the string "fizz."
# 2. if input is divisible by 5, it returns buzz
# 3. if divisible by both 3 and 5, returns FizzBuzz
# For any other numbers, returns the same number
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return (f"fizz_buzz")
    if input % 3 == 0:
        return (f"fizz")
    if input % 5 == 0:
        return (f"buzz")
    else:
        return input


print(fizz_buzz(15))
