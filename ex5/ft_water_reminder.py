def ft_water_reminder():
    waterDays = int(input("Days since last watering: "))
    if waterDays > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
