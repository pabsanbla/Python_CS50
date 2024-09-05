emoticon = "v.v" #global variable


def main():
    global emoticon #able to modify a global variable
    say("Is anyone there? ")
    emoticon = ":D"
    say("Oh, hi!")

def say(phrase):
    print(phrase + " " + emoticon)


main()
