"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# x is 10, y is 2.25, z is "I like turtles!"

# the printf operator (%)
print("x is %d, y is %.2f, z is '%s'" % (x, y, z)) 
    # %[flags][width][.precision]type
    # why don't I need to specify the [flags] or [width]?
    # (https://www.geeksforgeeks.org/python-output-formatting/#targetText=In%20Python%2C%20there%20is%20no,sometimes%20even%20called%20modulus)%20operator.)

# the 'format' string method
print("x is {}, y is {:.2f}, z is '{}'".format(x, y, z))

# using an f-string
print(f'x is {x}, y is {y:.2f}, z is "{z}"') # also works
print(f'x is {x}, y is {round(y, 2)}, z is "{z}"')