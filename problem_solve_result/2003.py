def sliding_window(nums, target_number):
    window_start = 0
    window_sum = 0
    counter = 0

    for window_end in range(len(nums)):
        window_sum += nums[window_end]
        # print(window_sum)

        while window_sum >= target_number:
            if window_sum == target_number:
                counter += 1

            window_sum -= nums[window_start]
            window_start += 1
            # if window_sum == target_number:
            #     counter += 1

    return counter


if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    result = sliding_window(arr, m)
    print(result)