import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #to avoid any invalid number hours = 0-12 / minutes = 00-59
    hours = r"0|1[0-2]|[1-9]"
    minutes = r"0[0-9]|[1-5][0-9]"
    try:
        if matches := re.search(rf"^({hours}):?({minutes})? (AM|PM) to ({hours}):?({minutes})? (AM|PM)$", s):
            int_time = list(matches.groups())
            int_operations(int_time)
            check_minutes(int_time)
            return f"{int_time[0]:02}:{int_time[1]} to {int_time[3]:02}:{int_time[4]}"
        else:
            raise ValueError
    except ValueError:
        sys.exit("ValueError")


def int_operations(hours):
    #convert to int
    hours[0] = int(hours[0])
    hours[3] = int(hours[3])
    #operate
    if hours[2] == "PM" and hours[0] != 12:
        hours[0] += 12
    if hours[5] == "PM" and hours[3] != 12:
        hours[3] += 12
    #special case
    if hours[2] == "AM" and hours[0] == 12:
        hours[0] = 0
    if hours[5] == "AM" and hours[3] == 12:
        hours[3] = 0


def check_minutes(minutes):
    if minutes[1] == None:
        minutes[1] = "00"
    if minutes[4] == None:
        minutes[4] = "00"

if __name__ == "__main__":
    main()
