# A lambda function to calculate the square of a number
square = lambda x: x * x

# Using lambda with map() to apply the function to a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

# Using lambda with filter() to filter odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)