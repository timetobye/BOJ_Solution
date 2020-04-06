from sys import stdin


def make_arrays(size):
    vector_arr = []
    
    x_axis_max = 0
    y_axis_max = 0
    
    for _ in range(size):
        x, y, = [int(x) for x in stdin.readline().split()]
    
        vector_arr.append([x, y])
    
        if x >= x_axis_max:
            x_axis_max = x
    
        if y >= y_axis_max:
            y_axis_max = y
    
    x_axis_max += 10
    y_axis_max += 10

    paper_arr = [[0 for j in range(x_axis_max)] for i in range(y_axis_max)]
    
    return paper_arr, vector_arr


def get_black_area_sum(paper_arr, vector_arr):
    cnt = 0
    for vector in vector_arr:
        x_value, y_value = vector
    
        for i in range(y_value, y_value + 10):
            for j in range(x_value, x_value + 10):
    
                if paper_arr[i][j] == 0:
                    paper_arr[i][j] = 1
                    cnt += 1
                    
    return cnt


def main():
    n = int(input())
    paper_arr, vector_arr = make_arrays(n)
    result = get_black_area_sum(paper_arr, vector_arr)

    print(result)


if __name__ == "__main__":
    main()







