n = 1000

list_of_ints = list(range(1, n))

three_or_five_multiples = [x for x in list_of_ints if x % 3 == 0 or x % 5 == 0]

print(sum(three_or_five_multiples))

