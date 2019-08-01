def find_solution(n):
    while True:
        value = int(input())

        if value == 0:
            break

        if value % n == 0:
            correct_answer_sting = f'{value} is a multiple of {n}.'
            print(correct_answer_sting)
        else:
            wrong_answer_string = f'{value} is NOT a multiple of {n}.'
            print(wrong_answer_string)


if __name__ == "__main__":
    n = int(input())
    find_solution(n)