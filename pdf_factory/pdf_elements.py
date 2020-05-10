from . import pdfFileSettings
from reportlab.pdfgen import canvas, textobject


class TextBlock:
    PFS = pdfFileSettings.PdfFileSettings
    to = None
    o_x = 0
    o_y = PFS.height

    def __init__(self, x: float, y: float):
        pass


