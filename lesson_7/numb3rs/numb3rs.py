import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    number_pattern = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
    ip_value = rf"^{number_pattern}\.{number_pattern}\.{number_pattern}\.{number_pattern}$"
    if matches := re.search(ip_value, ip.strip()):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
