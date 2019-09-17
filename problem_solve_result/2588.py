"""
base_number에 target_number의 속성값들을 곱해준다.
그리고 자릿수에 맞춰서 10**n을 해준다.

ex)472 * 385
= 472 * 5 * 10**0 + 472 * 8 * 10**1 + 472 * 3 * 10**2
"""


base_number = int(input())
target_number = reversed(input())
multiple_value = 0

for i, target_number_component in enumerate(target_number):
    midterm_value = base_number * int(target_number_component)
    multiple_value += midterm_value * (10**i)
    print(midterm_value)
print(multiple_value)