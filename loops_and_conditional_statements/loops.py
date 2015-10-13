from random import randint


# 1.1: function containing a loop that iterates over a range of values, 1-50. Return those values.
def loop_range(s=1, e=51):
    return range(s, e)


# 1.2: function containing a loop that iterates over a range of values, 0-50,
# skipping every odd number. Return the unskipped values. Use 'continue' for this.
# (Another solution, if continue is not neccesary, is ussing list comprehensions)
def loop_range_even(s=0, e=51):
    even_range = []
    for i in xrange(s, e):
        if i % 2 == 1:          # check if the number is odd
            continue            # don't process it
        even_range.append(i)
    return even_range


# 1.3: function containing loop that iterates, generating random integers between 1 and 100,
# stopping when the returned number is 42. Return the numbers generated up to this point.
def loop_random_values(min=1, max=100):
    random_ints = []
    while True:
        i = randint(min, max)
        if i == 42:
            break
        random_ints.append(i)
    return random_ints
