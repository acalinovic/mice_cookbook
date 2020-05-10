from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm


class PdfFileSettings:
    page_format = A4
    page_unit = mm
    width, height = page_format[0], page_format[1]
    top_m, right_m, bottom_m, left_m = 0, 0, 0, 0
    x, y = 0, page_format[1]
    cols = 1
    col_w = page_format[0]
    tabs = list()
    header_h, footer_h = 0, 0
    header_p, footer_p = 0, 0
    border_p = 0

    header_o = (left_m, height - top_m - header_h)
    header_d = (width - left_m - right_m, header_h)

    footer_o = (left_m, bottom_m)
    footer_d = (width - left_m - right_m, footer_h)

    ##
    # Force recomputing of all values
    @staticmethod
    def compute():
        PFS = PdfFileSettings
        page_unit = PFS.page_unit
        PFS.width *= page_unit
        PFS.height *= page_unit
        PFS.top_m *= page_unit
        PFS.right_m *= page_unit
        PFS.bottom_m *= page_unit
        PFS.left_m *= page_unit
        PFS.x *= page_unit
        PFS.y *= page_unit
        PFS.col_w = (PFS.width - PFS.left_m - PFS.right_m) / PFS.cols
        PFS.col_w *= page_unit
        PFS.header_h *= page_unit
        PFS.header_p *= page_unit
        PFS.footer_h *= page_unit
        PFS.footer_p *= page_unit
        PFS.border_p *= page_unit

        PFS.header_o = (PFS.left_m, PFS.height - PFS.top_m - PFS.header_h)
        PFS.header_d = (PFS.width - PFS.left_m - PFS.right_m, PFS.header_h)

        PFS.footer_o = (PFS.left_m, PFS.bottom_m)
        PFS.footer_d = (PFS.width - PFS.left_m - PFS.right_m, PFS.footer_h)

    ##
    # Sets PDF page format
    # @param page_size Width and height
    # @param unit Unit factor
    @staticmethod
    def set_format(page_size: tuple, unit: float):
        PdfFileSettings.page_format = page_size
        PdfFileSettings.page_unit = unit
        PdfFileSettings.width = page_size[0]
        PdfFileSettings.height = page_size[1]
        PdfFileSettings.compute()

    ##
    # Sets PDF margins
    # @param top Top page margin value in page unit
    # @param right Right page margin value in page unit
    # @param bottom Bottom page margin in page unit
    # @param left Left page margin in page unit
    @staticmethod
    def set_page_margins(top: float, right: float, bottom: float, left: float):
        PdfFileSettings.top_m = top * PdfFileSettings.page_unit
        PdfFileSettings.right_m = right * PdfFileSettings.page_unit
        PdfFileSettings.bottom_m = bottom * PdfFileSettings.page_unit
        PdfFileSettings.left_m = left * PdfFileSettings.page_unit
        PdfFileSettings.compute()

    ##
    # Sets PDF number of columns
    # @param number Number of columns
    @staticmethod
    def set_cols(number: int):
        PdfFileSettings.cols = number
        PdfFileSettings.compute()

    ##
    # Sets PDF list of tabulations
    # @param tab_list Lengths of tabulations in page unit
    @staticmethod
    def set_tabs(tab_list: list):
        PdfFileSettings.tabs = list()
        for i in tab_list:
            PdfFileSettings.tabs.append(i)
        PdfFileSettings.compute()

    ##
    # Sets PDF header
    # @param height Header's height in page unit
    # @param padding Header's padding in page unit
    @staticmethod
    def set_header(height: float, padding: float):
        PdfFileSettings.header_h = height * PdfFileSettings.page_unit
        PdfFileSettings.header_p = padding * PdfFileSettings.page_unit
        PdfFileSettings.compute()

    ##
    # Sets PDF footer
    # @param height Footer's height in page unit
    # @param padding Footer's padding in page unit
    @staticmethod
    def set_footer(height: float, padding: float):
        PdfFileSettings.footer_h = height * PdfFileSettings.page_unit
        PdfFileSettings.footer_p = padding * PdfFileSettings.page_unit
        PdfFileSettings.compute()

