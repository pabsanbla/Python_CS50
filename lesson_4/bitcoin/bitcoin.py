import sys
import requests

def main():
    #input from the command line
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    #once we got a command
    try:
        bitcoin =float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument it´s not a number")

    print(f"${bitcoin_price(bitcoin):,.4f}")


def bitcoin_price(amount):
    try:
        answer = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit()

    object = answer.json()
    bpi = object["bpi"]
    monetary_base = bpi["USD"]
    return monetary_base["rate_float"] * amount


main()




