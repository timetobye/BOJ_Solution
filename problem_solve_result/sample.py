from os import listdir
from bs4 import BeautifulSoup
import requests


"""
마크다운을 이용해 문제 풀이 결과를 적기 위한 코드입니다.
- 디렉토리 내 파일 리스트를 가져옵니다.
- 그리고 문항 번호를 슬라이싱 해서 웹에서 정보를 가져옵니다.
- 마크다운 양식에 맞게 프린트 한 후 정리합니다.

# Result
|알고리즘|문항번호 + 문제 url|문제 이름|성공 여부|비고|
|---|---|---|---|---|

"""


def get_parsing_file_list():
    parsing_file_list = []

    current_folder_file_names = listdir('.')

    for file_name in current_folder_file_names:
        if file_name[-2:] == 'py':
            parsing_file_list.append(file_name)

    return parsing_file_list


def func(x):
    return x[:-2]


def sort_file_list(parsing_file_list):
    sorted_file_list = sorted(parsing_file_list, key=func)

    return sorted_file_list


def print_markdown_form(sorted_file_list):
    base_url = f'https://www.acmicpc.net/problem/'

    for i, number in enumerate(sorted_file_list):
        problem_url = base_url + number[:-3]
        try:
            requests_result = requests.get(problem_url)
            res_soup = BeautifulSoup(requests_result.text, 'html.parser')
            problem_title = res_soup.find_all('span', id='problem_title')[0]

            print(f'|알고리즘|[{number[:-3]}](https://github.com/timetobye/BOJ_Solution/blob/master/'
                  f'{number})|{problem_title.text}|성공| |')

        except Exception as e:
            """숫자 문자열이 아니면"""
            pass


def main():
    parsing_file_list = get_parsing_file_list()
    sorted_file_list = sort_file_list(parsing_file_list)

    print_markdown_form(sorted_file_list)


if __name__ == "__main__":
    main()
