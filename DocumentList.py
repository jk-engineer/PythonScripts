# Программа для создания таблицы с обозначениями и наименованиями документов PDF.
# Copyright (C) 2020 Evgeniy Ipatov

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


import os
import sys
from os import listdir
from os.path import isfile, join
from docx import Document


# Получение текущей директории
current_directory = os.path.dirname(os.path.abspath(__file__))
# Получение имен файлов, имеющихся в текущей директории
file_names = [name for name in listdir(current_directory) if isfile(join(current_directory, name))]
# Выбор файлов с расширением pdf
file_names = [name for name in file_names if os.path.splitext(name.lower())[1] == '.pdf']
file_names.sort()

# Выход из программы при отсутствии файлов pdf
if len(file_names) == 0:
    print('\nНе найдены файлы pdf. Завершение работы программы')
    sys.exit()

# Составление таблицы с порядковым номером, обозначением, наименованием документа
documents_count = len(file_names)
output_data = []
for index in range(0, documents_count):
    # Разделение имени файла на обозначение и наименование
    file_name = os.path.splitext(file_names[index])[0]
    values = file_name.split()
    if values[1] == 'СБ':
        part_number = values[0] + values[1]
        part_title = ' '.join(values[2:])
    else:
        part_number = values[0]
        part_title = ' '.join(values[1:])
    output_data.append([str(index + 1), part_number, part_title])

# Запись данных в файл в виде таблицы
document = Document()
table = document.add_table(rows=1, cols=3)
# Шапка таблицы
hdr_cells = table.rows[0].cells
hdr_cells[0].text = '№ п/п'
hdr_cells[1].text = 'Обозначение'
hdr_cells[2].text = 'Наименование'
# Порядковый номер, обозначение, наименование документа
for number, p_number, p_title in output_data:
    row_cells = table.add_row().cells
    row_cells[0].text = number
    row_cells[1].text = p_number
    row_cells[2].text = p_title
# Итоговое количество документов
row_cells = table.add_row().cells
row_cells[0].text = ''
row_cells[1].text = 'Итого документов:'
row_cells[2].text = str(documents_count)
# Сохранение документа
report_file_name = '!Список документов.docx'
document.save(report_file_name)
# Отчет о завершении работы
print('\nСписок документов сохранен в файле \"' + report_file_name + '\"')
