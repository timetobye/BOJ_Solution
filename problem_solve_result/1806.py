def find_sub_sum(nums, target):
    window_start = 0
    min_length = 100001
    # num_length = len(num)
    sub_sum = 0

    for window_end, value in enumerate(nums):
        sub_sum += value
        # print(sub_sum, min_length)

        while sub_sum >= target:
            window_size = window_end - window_start + 1
            # print(f'window size : {window_size}')
            min_length = min(min_length, window_size)
            
            sub_sum -= nums[window_start]
            # print(f'sub_sum : {sub_sum}')
            window_start += 1

    if min_length == 100001:
        return 0
            
    return min_length


if __name__ == "__main__":
    n, s = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    result = find_sub_sum(arr, s)
    print(result)