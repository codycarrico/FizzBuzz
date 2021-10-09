# Starting the loop, range from 1-100
for i in range(1,100):
    # Checking modulus of BOTH 5 and 3 for FizzBuzz
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    # Checking modulus of 5 for Buzz
    elif i % 5 == 0:
        print("Buzz")
    # Checking modulus of 3 for Fizz
    elif i % 3 == 0:
        print("Fizz")
    # Printing numbers that are neither Fizz nor Buzz
    else: print(i)
