# Программа для сортировки страниц PDF-файлов по форматам.
# Copyright (C) 2019 - 2020 Evgeniy Ipatov

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
from PyPDF2 import PdfFileReader, PdfFileWriter


def check_size(standard_value, current_value):
    """Возвращает результат проверки соответствия размера формата листа требованиям ГОСТ 2.301.

    :param standard_value: стандартное значение размера по ГОСТ 2.301.
    :param current_value: проверяемое значение.
    """
    if standard_value <= 150 and abs(standard_value - current_value) <= 1.5:
        return True
    elif 150 < standard_value <= 600 and abs(standard_value - current_value) <= 2.0:
        return True
    elif standard_value > 600 and abs(standard_value - current_value) <= 3.0:
        return True
    else:
        return False


# Выбор файлов с расширением pdf
p = pathlib.Path('.').glob('*.pdf')
file_names = sorted([name for name in p if name.is_file()])

# Выход из программы при отсутствии файлов pdf
if len(file_names) == 0:
    print('\nНе найдены файлы pdf. Завершение работы программы')
    sys.exit()

# Размеры форматов по ГОСТ 2.301
sheet_size_height = {
    'A0': 841,
    'A1': 594,
    'A2': 420,
    'A3': 297,
    'A4': 210,
    'A5': 148,
    'A0x2': 1189,
    'A0x3': 1189,
    'A1x3': 841,
    'A1x4': 841,
    'A2x3': 594,
    'A2x4': 594,
    'A2x5': 594,
    'A3x3': 420,
    'A3x4': 420,
    'A3x5': 420,
    'A3x6': 420,
    'A3x7': 420,
    'A4x3': 297,
    'A4x4': 297,
    'A4x5': 297,
    'A4x6': 297,
    'A4x7': 297,
    'A4x8': 297,
    'A4x9': 297
}

sheet_size_width = {
    'A0': 1189,
    'A1': 841,
    'A2': 594,
    'A3': 420,
    'A4': 297,
    'A5': 210,
    'A0x2': 1682,
    'A0x3': 2523,
    'A1x3': 1783,
    'A1x4': 2378,
    'A2x3': 1261,
    'A2x4': 1682,
    'A2x5': 2102,
    'A3x3': 891,
    'A3x4': 1189,
    'A3x5': 1486,
    'A3x6': 1783,
    'A3x7': 2080,
    'A4x3': 630,
    'A4x4': 841,
    'A4x5': 1051,
    'A4x6': 1261,
    'A4x7': 1471,
    'A4x8': 1682,
    'A4x9': 1892
}

# Удаление файлов с именами, совпадающими с названиями форматов
non_standard = 'A_NonStandard'
reserved_names = [name + '.pdf' for name in sheet_size_height.keys()]
reserved_names.append(non_standard + '.pdf')
for name in reserved_names:
    if name.lower() in [str(name).lower() for name in file_names]:
        del_name = pathlib.Path(name)
        del_name.unlink()
        file_names.remove(del_name)

convert_pt_to_mm = 25.4 / 72.0
output_data = {}
output_data[non_standard] = PdfFileWriter()
for key in sheet_size_height.keys():
    output_data[key] = PdfFileWriter()

# Считывание листов из файла PDF и сортировка их по форматам
read_streams = []
for name in file_names:
    read_streams.append(open(name, 'rb'))
    pdf_document = PdfFileReader(read_streams[-1])
    pages_count = pdf_document.getNumPages()
    for index in range(0, pages_count):
        current_page = pdf_document.getPage(index)
        page_added = False
        # Размеры страницы необходимо перевести из пунктов в мм
        page_height = round(float(current_page.mediaBox.getHeight()) * convert_pt_to_mm)
        page_width = round(float(current_page.mediaBox.getWidth()) * convert_pt_to_mm)
        for key in sheet_size_height.keys():
            standard_height = sheet_size_height[key]
            standard_width = sheet_size_width[key]
            # Проверяются альбомные и портретные ориентации листа
            if (check_size(standard_height, page_height) and check_size(standard_width, page_width)) or (check_size(standard_width, page_height) and check_size(standard_height, page_width)):
                output_data[key].addPage(current_page)
                page_added = True
                break
        if not page_added:
            output_data[non_standard].addPage(current_page)

# Сохранение отсортированных страниц в файлы с названиями форматов
output_file_names = []
for key in output_data.keys():
    if output_data[key].getNumPages() != 0:
        f_name = key + '.pdf'
        output_file_names.append(f_name)
        with open(f_name, 'wb') as out_stream:
            output_data[key].write(out_stream)
# Закрытие потоков чтения файлов
for stream in read_streams:
    stream.close()
# Отчет о завершении работы
print('\nСортировка по форматам завершена. Созданы следующие файлы:\n')
print('\n'.join(output_file_names) + '\n')
