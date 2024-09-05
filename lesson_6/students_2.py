import csv

name = input("What´s your name? ")
home = input("Where´s your home? ")
#write instead of read
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
