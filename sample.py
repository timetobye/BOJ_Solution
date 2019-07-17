from os import listdir
from pprint import pprint
from bs4 import BeautifulSoup
import requests


files = listdir('.')

real = []

for file in files:
    if file[-2:] =='py':
        real.append(file)


def func(x):
    return x[:-2]


value = sorted(real, key=func)

base_url = f'https://www.acmicpc.net/problem/'


for i, number in enumerate(value):
    try:
        problem_url = base_url + number[:-3]
        # problem_url = base_url + '1005'

        # print(problem_url)
        requests_result = requests.get(problem_url)

        res_soup = BeautifulSoup(requests_result.text, 'html.parser')
        problem_title = res_soup.find_all('span', id='problem_title')[0]

        # print(problem_title.text)
        print(f'|알고리즘 종류|[{number[:-3]}](https://github.com/timetobye/BOJ_Solution/blob/master/{number})|{problem_title.text}|성공| |')

        #
        # if i==0:
        #     break

        # print(res_soup)

    except:
        """테스트 용도 입니다."""
        pass





#
# |알고리즘 종류   |문항번호   |문제 이름   |성공 여부|비고|
# |---|---|---|---|---|