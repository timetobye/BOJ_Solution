def main():
    max_count_passengers = 0
    count_passenger = 0
    for _ in range(4):
        off_passenger_count, on_passenger_count = [int(x) for x in input().split()]
        off_passenger_count *= -1

        count_passenger += off_passenger_count
        count_passenger += on_passenger_count

        if count_passenger > max_count_passengers:
            max_count_passengers = count_passenger

    print(max_count_passengers)


if __name__ == "__main__":
    main()
