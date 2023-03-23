# Программа для добавления литеры в основную надпись КД в формате PDF.
# Copyright (C) 2022 Evgeniy Ipatov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import pathlib
import sys
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder


# Выбор файлов с расширением pdf
p = pathlib.Path('.').glob('*.pdf')
file_names = sorted([name for name in p if name.is_file()])

# Выход из программы при отсутствии файлов pdf
if len(file_names) == 0:
    print('\nНе найдены файлы pdf. Завершение работы программы')
    sys.exit()

documents_count = len(file_names)
convert_pt_to_mm = 25.4 / 72.0
for name in file_names:
    in_stream = open(name, 'rb')
    pdf_document = PdfReader(in_stream)
    first_page = pdf_document.pages[0]
    litera_text = AnnotationBuilder.free_text(
        'O',
        rect=(50, 50, 100, 100),
        font='Arial',
        bold=False,
        italic=False,
        font_size='20pt',
        font_color='000000',
        border_color='000000',
        background_color='ffffff'
    )
    writer = PdfWriter()
    writer.add_page(first_page)
    writer.add_annotation(page_number=0, annotation=litera_text)

with open("annotated-pdf.pdf", "wb") as fp:
    writer.write(fp)
