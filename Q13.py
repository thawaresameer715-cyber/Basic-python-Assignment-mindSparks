#13. Use list comprehension with if to filter even numbers from 1-50 into a tuple.

even_numbers = tuple([x for x in range(1, 51) if x % 2 == 0])

print(even_numbers)