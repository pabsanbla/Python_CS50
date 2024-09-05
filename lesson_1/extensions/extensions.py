def main():
    extension = input("File name: ").lower().strip()
    
    if extension.endswith(".gif"):
        print("image/gif")
    elif extension.endswith(".jpg") | extension.endswith(".jpeg"):
        print("image/jpeg")
    elif extension.endswith(".png"):
        print("image/png")
    elif extension.endswith(".pdf"):
        print("application/pdf")
    elif extension.endswith(".txt"):
        print("text/plain")
    elif extension.endswith(".zip"):
        print("application/zip")
    else :
        print("application/octet-stream")


main()





