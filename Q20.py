#Prime finder: Loop 1-100, check primality with while/for, store in set, list primes in dict by digit sum.

primes = set()

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.add(num)

digit_sum_dict = {}

for p in sorted(primes):
    d_sum = sum(int(digit) for digit in str(p))
    
    if d_sum not in digit_sum_dict:
        digit_sum_dict[d_sum] = []
    digit_sum_dict[d_sum].append(p)

for d_sum, p_list in sorted(digit_sum_dict.items()):
    print(f"Digit Sum {d_sum}: {p_list}")