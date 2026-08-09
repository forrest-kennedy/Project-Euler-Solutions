import math

n = 600851475143

possible_factors = list(range(1, math.floor(math.sqrt(n))))
factors = [x for x in possible_factors if n % x == 0]

print(factors)
print(max(factors))






