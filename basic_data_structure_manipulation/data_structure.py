from random import randint
from loops_and_conditional_statements.loops import loop_random_values, loop_range


# 2.1: function that sorts the numbers generated in loops.loop_random_values in ascending order.
def sort_random_values():
    values = loop_random_values()
    values.sort()               # in-place sorting
    return values


# 2.2: function that filters the numbers returned by the method implemented in loop_random_values
# so they match loop_range
def filter_random_values():
    range_values = loop_range()
    random_values = loop_random_values()
    match_values = []
    for i in random_values:
        if i in range_values:
            match_values.append(i)
    return match_values


# 2.3: lambda function that returns the same output of 1.2 (default values (0,51) )
range_even = lambda start=0, end=51: [i for i in xrange(start, end) if i % 2 == 0]


# 2.4: lambda function that returns a dictionary of the form `{0: 1, 1: 2, 2: 3, ..., 9: 10}`
dictionary = lambda end=10: {k: k+1 for k in xrange(end)}


# 2.5: 1.1, 1.2, 1.3, 2.1, and 2.2 as generators.
# 1.1: loop_range
gen_loop_range = (i for i in xrange(1, 51))

# 1.2: loop_range_even
gen_range_even = (i for i in xrange(0, 51) if i % 2 == 0)


# 1.3: loop_random_values
def gen_random_values(min=1, max=100):
    while True:
        i = randint(min, max)
        if i == 42:
            break
        yield i


# 2.1: sort_random_values
def gen_sort_random_values():
    values = loop_random_values()
    values.sort()
    for value in values:
        yield value


# 2.2: filter_random_values
def gen_filter_random_values():
    range_values = loop_range()
    random_values = loop_random_values()
    for i in random_values:
        if i in range_values:
            yield i
