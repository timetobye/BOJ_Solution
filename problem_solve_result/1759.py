from itertools import combinations


def get_possible_combinations(password_length, password_possible_character_list):
    vowels = ['a', 'e', 'i', 'o', 'u']

    for combination in combinations(password_possible_character_list, password_length):
        vowel_count = len([character for character in combination if character in vowels])
        consonant_count = len([character for character in combination if character not in vowels])

        if vowel_count >= 1 and consonant_count >= 2:
            result = "".join(combination)
            print(result)


def main():
    length, character_count = [int(x) for x in input().split()]
    character_list = sorted(input().split())
    get_possible_combinations(length, character_list)


if __name__ == "__main__":
    main()
