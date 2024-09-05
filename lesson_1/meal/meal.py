def main():
    time = input("What time is it? ")
    meal = convert(time)
    if meal >= 7 and meal <=8:
        print("breakfast time")
    elif meal >= 12 and meal <= 13:
        print("lunch time")
    elif meal >= 18 and meal <= 19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60.0 #convert into 6 base
    return hours + minutes


if __name__ == "__main__":
    main()
