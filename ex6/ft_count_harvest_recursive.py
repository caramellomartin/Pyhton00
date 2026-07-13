def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    def helper(current_day):
        if current_day < (days + 1):
            print(f"Day {current_day}")
            helper(current_day + 1)
        else:
            print(f"Harvest time!")
    helper(1)
