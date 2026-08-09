top = 1
bottom = 978000

list_of_numbers = list(range(top, bottom))
list_of_odd_squares = [x**2 for x in list_of_numbers if x % 2 == 1]

print(sum(list_of_odd_squares))
