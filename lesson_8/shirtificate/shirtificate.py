from fpdf import FPDF


def main():
    name = input("Name: ")
    create_shirtificate(name)


def create_shirtificate(name):
    pdf = FPDF(orientation="P", format="A4") #by default
    pdf.add_page()

    #Header
    pdf.set_font("Helvetica", "B", 36)  #Helvetic, Bold, size = 36
    pdf.set_y(20)
    pdf.cell(0, 0, "CS50 Shirtificate", align="C", center=True) #Center

    #Add the image
    pdf.image("shirtificate.png", x="C", y=50, w=190)

    #Message configuration
    pdf.set_font("Helvetica", "", 28) #Helvetic, normal, size = 28
    pdf.set_text_color(255, 255, 255)  #White

    #Message
    pdf.set_y(120)
    pdf.cell(0, 0, f"{name} took CS50", align="C", center=True)  #Center

    #Save pdf
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
