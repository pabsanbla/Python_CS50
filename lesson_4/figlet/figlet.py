import random
import sys
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    font_list = figlet.getFonts()
    if len(sys.argv) == 1:
        #random font
        figlet.setFont(font=random.choice(font_list))
        print(figlet.renderText(input("Input: ")))
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
        #especific
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(input("Input: ")))
    else:
        #bad input
        sys.exit("Invalid usage")


main()
