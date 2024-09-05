import sys
from PIL import Image, ImageOps

def main():
    conditions(sys.argv[1:]) #send command-line except file name
    try:
        input_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist") #last fail
    else:
        #to know the size
        shirt = Image.open("shirt.png")
        size = shirt.size
        #adjust
        sized_image = ImageOps.fit(input_image, size)
        #overwrite
        sized_image.paste(shirt, shirt)
        #save
        sized_image.save(sys.argv[2])


def conditions(prompt):
    archive_format = ["jpg", "jpeg", "png"] #OK formats
    if len(prompt) < 2:
        sys.exit("Too few command-line arguments") #excess
    elif len(prompt) > 2:
        sys.exit("Too many command-line arguments") #fault
    elif  not extension(prompt[0]) in archive_format:
        sys.exit("Invalid input") #bad input
    elif not extension(prompt[1]) in archive_format:
        sys.exit("Invalid output") #bad output
    elif extension(prompt[0]) != extension(prompt[1]):
        sys.exit("Input and output have different extensions") #different format



def extension(path):
    #returns the extension
    ext = path.split(".")
    return ext[1].lower()

if __name__ == "__main__":
    main()
