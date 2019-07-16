from os import listdir

files = listdir('.')

real = []

for file in files:
    if file[-2:] =='py':
        real.append(file)


def func(x):
    return x[:-2]


value = sorted(real, key=func)


for number in value:
    print(f'|알고리즘 종류|[{number[:-3]}](https://github.com/timetobye/BOJ_Solution/blob/master/{number})|문제 이름|성공| |')


#
# |알고리즘 종류   |문항번호   |문제 이름   |성공 여부|비고|
# |---|---|---|---|---|