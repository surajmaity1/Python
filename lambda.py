# note: Use lambda functions when an anonymous function is required for a short period of time.

add = lambda num1, num2: num1 + num2

result = add(2, 3)
print(result)


# Anonymous function inside another function
def add_with(value):
    return lambda a: a + value


result1 = add_with(21)
result2 = add_with(21)
print(result1(3))
print(result2(23))

