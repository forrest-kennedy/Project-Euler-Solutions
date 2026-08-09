fib_seq = [1]

new_entry = 2

while(new_entry < 4000000):
    fib_seq.append(new_entry)
    new_entry = fib_seq[-1] + fib_seq[-2]

even_fib_seq = [x for x in fib_seq if x % 2 == 0]

print(sum(even_fib_seq))
