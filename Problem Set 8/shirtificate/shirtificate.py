from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        page_width = self.w
        x = (page_width - 180) / 2
        self.image("shirtificate.png",x=x,y= 60,w = 180)


        self.set_font("helvetica", style="B", size=30)

        self.set_y(10)
        title_width = self.get_string_width(self.title) + 6
        self.set_x((page_width - title_width) / 2)
        self.cell(title_width, 10, self.title)

    def shirt_body(self, name):
        context = f"{name} took CS50"
        self.set_font("helvetica", size=18)
        self.set_text_color(255, 255, 255)
        self.set_y(110)
        self.cell(0, 10, context, align="C")



pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.set_title("CS50 Shirtificate")
name = input("Name: ")
pdf.add_page()
pdf.shirt_body(name)
pdf.output("shirtificate.pdf")


