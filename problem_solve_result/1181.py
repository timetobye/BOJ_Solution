"""
1. 얼마만큼 문자열 집합을 만들지는 주어지는 문자열 중 가장 긴 것이 결정한다.
2. 구상은 이렇게 된다 [ [ ], [ ], [ ], [ ].....[ ]]
문자열 길이별로 넣은 후에 각각 정렬
동일 단어는 지워야 할 듯
3. 그리고 출력한다.
"""
from sys import stdin


def create_word_components(n):
    word_components = [[] for i in range(51)]
    for i in range(n):
        word = stdin.readline().strip()
        word_length = len(word)

        if word not in word_components[word_length]:
            word_components[word_length].append(word)

    return word_components


def sort_component(word_list):
    word_list = sorted(word_list, key=lambda x: x)

    return word_list


def main():
    n = int(input())
    word_components = create_word_components(n)

    result_words = []
    for i, word_component in enumerate(word_components):
        if word_component:
            result_words += sort_component(word_component)

    for word in result_words:
        print(word)


if __name__ == "__main__":
    main()