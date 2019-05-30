# problem 6 (https://projecteuler.net/problem=6)
diff_between_sum_of_squares = sum([x for x in range(100)]) ** 2 - sum([x**2 for x in range(100)])
print(diff_between_sum_of_squares)

# problem 9
pythagorean_triplet = [(a, b, (1000-a-b)) for a in range(1, 1000) \
                       for b in range(a, 1000) if a**2 + b**2 == (1000-a-b)**2]
print(pythagorean_triplet)

# problem 48
sum_of_digit = str(sum([x**x for x in range(1, 1001)]))[-10:]
print(sum_of_digit)