import inflect

def main():
    answer = inflect.engine() #in order to use it
    name_list = [] #void list
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            answer = answer.join(name_list)
            return print("Adieu, adieu, to " + answer)
        else:
            name_list.append(name) #increment the list


main()
