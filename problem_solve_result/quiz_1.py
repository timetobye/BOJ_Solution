"""
Q. text가 주어질 때 word의 애너그램이 text안에 존재하는지 확인하는 코드를 작성하라

sample text and word
​
case 1.
text : thecatissocute
word : act
​
case 2.
text : waitressisniceandkind
word : rest, ress
​
"""


def count_char(word):
    """
    단어가 가지고 있는 문자의 개수를 센다.
    """
    char_list = list(word)
    char_counter = {}

    for char in char_list:
        if char not in char_counter:
            char_counter[char] = 1
        else:
            char_counter[char] += 1

    return char_counter


def check_anagram(counter, token):
    chars = list(token)

    for char in chars:
        if char in counter:
            counter[char] -= 1

    results = list(counter.values())

    for result in results:
        if result != 0:
            break
    else:
        print(f'Anagram is in text : {token}')


def main():
    text = input()
    word = input()

    text_length = len(text)
    word_length = len(word)
    search_length = text_length - word_length + 1

    count_result = count_char(word)

    for idx in range(search_length):
        indexed_text = text[idx:idx + word_length]
        check_anagram(count_result.copy(), indexed_text)


if __name__ == "__main__":
    main()
