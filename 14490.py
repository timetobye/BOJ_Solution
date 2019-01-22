from math import gcd

n, m = map(int, input().split(':'))
gcd_value = gcd(n, m)

new_n = n // gcd_value
new_m = m // gcd_value

print(f'{new_n}:{new_m}')