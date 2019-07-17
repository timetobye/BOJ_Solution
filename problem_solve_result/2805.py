
'''
재귀 이용

def search(start,end,tree,k):
    mid=(start+end)//2   # 중간 지점 찾기
    sum_lst=0
    for t_height in tree:
        if t_height > mid:
            sum_lst += (t_height - mid)
    if sum_lst == k:
        print(mid)
    elif sum_lst > k:
        if (end - start) <=1:
            print(start)
        else:
            search(mid, end, tree,k)
    else:
        search(start,mid,tree,k)

n,k= map(int,input().split())
tree = list(map(int, input().split()))
start = 0
end = max(tree)
search(start,end,tree,k)

'''

'''
while 이용

import sys
def binary_search(end, tree, k):
    start = 0

    while True:
        mid = (start + end) // 2
        check = mid
        sum_lst = 0
        for t_height in tree:
            if t_height > check:
                sum_lst += (t_height - check)
        if sum_lst == k:
            print(check)
            break      
        elif sum_lst > k:
            if (end - start) <=1:
                print(start)
                break
            else:
                start = mid
        else:
            end = mid
n,k= map(int,sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
end = max(tree)
binary_search(end,tree,k)

'''