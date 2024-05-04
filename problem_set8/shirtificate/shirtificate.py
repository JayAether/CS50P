from fpdf import FPDF


def main():
    pdf = FPDF()

    pdf.add_page()

    page_width = pdf.w
    page_height = pdf.h

    name = input('Name: ')

    image(page_width, page_height, pdf)
    overlay(name, page_width, page_height, pdf)
    header(page_width, pdf)

    pdf.output('shirtificate.pdf')


def header(page_width, pdf):
    pdf.set_font("helvetica", "B", 40)

    text = 'CS50 Shirtificate'
    text_width = pdf.get_string_width(text) + 6

    x_position = (page_width - text_width) / 2

    pdf.set_xy(x_position, 10)
    pdf.cell(text_width, 10, text, 0, 1, 'C')


def overlay(user_input, page_width, page_height, pdf):
    pdf.set_font("helvetica", "B", 30)

    text = user_input + ' Took CS50'
    text_width = pdf.get_string_width(text) + 6
    text_height = pdf.font_size * 1.15

    x_position = (page_width - text_width) / 2
    y_position = (page_height - text_height) / 2 - 40

    pdf.set_xy(x_position, y_position)
    pdf.cell(text_width, text_height, text, 0, 1, 'C')


def image(page_width, page_height, pdf):
    image_size = 200

    x_position = (page_width - image_size) / 2
    y_position = (page_height - image_size) / 2

    pdf.image('shirtificate.png', x=x_position, y=y_position, w=image_size)


if __name__ == '__main__':
    main()
