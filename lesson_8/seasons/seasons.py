from datetime import date, datetime
import sys
import inflect


def main():
    aux = inflect.engine()  # in order to us inflect
    birth_date = check(input("Date of birth: "))
    actual_date = date.today()
    age = actual_date - birth_date
    minutes = int(age.total_seconds() / 60)  # Their life in minutes
    formated_age = aux.number_to_words(minutes, andword="")
    print(formated_age.capitalize() + " minutes")


def check(birth_date):
    try:
        return datetime.strptime(birth_date, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
