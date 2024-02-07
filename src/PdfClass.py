from fpdf import FPDF


class PDFCreation:
    def __init__(self):
        self.pdf = FPDF(unit="pt", format=(595, 842))
        self.font = "helvetica"

    def ajouter_page(self):
        self.pdf.add_page()

    def police(self, size=12):
        self.pdf.set_font(self.font, size=size)

    def souligner(self, x, y, text, font_size=12):
        self.pdf.set_xy(x, y)
        self.pdf.cell(0, 10, text)
        text_width = self.pdf.get_string_width(text)
        self.pdf.line(x, y + font_size * 0.35, x + text_width, y + font_size * 0.35)

    def ajouter_texte(self, x, y, text, max_width=None, underlined=0, font_size=12):
        self.pdf.set_xy(x, y)
        if underlined:
            self.souligner(x, y, text, font_size)
        if max_width is None:
            self.pdf.cell(0, 10, text)
        else:
            self.pdf.multi_cell(max_width, 14, text)

    def ajouter_image(self, x, y, file, w=0, h=0):
        self.pdf.image(file, x, y, w, h)

    def sauvegrader_pdf(self, filename):
        self.pdf.output(filename)
