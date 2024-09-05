months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
            date = input("Date: ").strip()
            try:
                if "/" in date:
                    month, day, year = date.split("/")
                    if int(day) <= 31 and int(month) <= 12:
                        print(f"{year}-{int(month):02}-{int(day):02}")
                    else:
                         raise ValueError
                else:
                    month, day, year = date.split()
                    if day == day.removesuffix(","):
                         raise ValueError
                    else:
                         day = day.removesuffix(",")
                    if int(day) <= 31:
                        print(f"{year}-{months.index(month)+1:02}-{int(day):02}")
                    else:
                         raise ValueError
                break
            except ValueError:
                 continue

main()
