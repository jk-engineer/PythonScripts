# Программа для подсчета количества форматов А4 в файлах PDF.
# Copyright (C) 2019 - 2021 Evgeniy Ipatov

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
from PyPDF2 import PdfFileReader


# Выбор файлов с расширением pdf
p = pathlib.Path('.').glob('*.pdf')
file_names = sorted([name for name in p if name.is_file()])

# Выход из программы при отсутствии файлов pdf
if len(file_names) == 0:
    print('\nНе найдены файлы pdf. Завершение работы программы')
    sys.exit()

# Подсчет количества форматов
documents_count = len(file_names)
summary_A4_count = 0
A4_size = 210 * 297
convert_pt_to_mm = 25.4 / 72.0
output_data = []
output_data.append('Документ:\tФорматов А4:\n\n')
for name in file_names:
    # Чтение файла pdf
    in_stream = open(name, 'rb')
    pdf_document = PdfFileReader(in_stream)
    # Количество листов в файле
    pages_count = pdf_document.getNumPages()
    # Подсчет количества форматов А4 в каждом листе
    # Алгоритм подсчета: вычисляется площадь каждого листа и делится на площадь формата А4. Полученное число округляется до целого.
    document_A4_count = 0
    for index in range(0, pages_count):
        current_page = pdf_document.getPage(index)
        # Размеры страницы необходимо перевести из пунктов в мм
        page_width = round(float(current_page.mediaBox.getWidth()) * convert_pt_to_mm)
        page_height = round(float(current_page.mediaBox.getHeight()) * convert_pt_to_mm)
        page_A4_count = round(page_width * page_height / A4_size)
        # Количество форматов А4
        document_A4_count += page_A4_count
        summary_A4_count += page_A4_count
    in_stream.close()
    output_data.append('\t'.join([str(name), str(document_A4_count)]))

output_data.append('\n\nИтого документов:\t' + str(documents_count))
output_data.append('\nИтого форматов А4:\t' + str(summary_A4_count))

# Запись данных в файл
report_file_name = '!Количество форматов.txt'
with open(report_file_name, 'w', encoding='utf-8') as out_stream:
    out_stream.write('\n'.join(output_data))
# Отчет о завершении работы
print('\nДокументов: ' + str(documents_count))
print('\nФорматов А4: ' + str(summary_A4_count))
print('\nПодсчет форматов завершен. Отчет сохранен в файле \"' + report_file_name + '\"')
