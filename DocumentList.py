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

# Коды документов
doc_codes = [
'СБ',
'ВО',
'ТЧ',
'ГЧ',
'МЭ',
'МЧ',
'УЧ',
'МС',
'ЭСБ',
'МД',
'Э1',
'Э2',
'Э3',
'Э4',
'Э5',
'Э6',
'Э7',
'ПЭ1',
'ПЭ2',
'ПЭ3',
'ПЭ4',
'ПЭ5',
'ПЭ6',
'ПЭ7',
'ТЭ4',
'ТЭ5',
'Э3.1',
'Э3.2',
'Э3.3',
'Э3.4',
'Э3.5',
'Э3.6',
'Э3.7',
'ПЭ3.1',
'ПЭ3.2',
'ПЭ3.3',
'ПЭ3.4',
'ПЭ3.5',
'ПЭ3.6',
'ПЭ3.7',
'Г1',
'Г2',
'Г3',
'Г4',
'Г5',
'Г6',
'Г7',
'ПГ1',
'ПГ2',
'ПГ3',
'ПГ4',
'ПГ5',
'ПГ6',
'ПГ7',
'ТГ4',
'ТГ5',
'П1',
'П2',
'П3',
'П4',
'П5',
'П6',
'П7',
'ПП1',
'ПП2',
'ПП3',
'ПП4',
'ПП5',
'ПП6',
'ПП7',
'ТП4',
'ТП5',
'К1',
'К2',
'К3',
'К4',
'К5',
'К6',
'К7',
'Д1',
'Д2',
'Д3',
'Д4',
'РЭ',
'РЭ1',
'РЭ2',
'РЭ3',
'ФО',
'ПС',
'ЗИ',
'РК',
'ВП',
'РР1',
'РР2',
'РР3',
'РР4',
'РР5',
'РР6',
'РР7',
'РР8',
'РР9',
'РР10',
'РР11',
'РР12',
'РР13',
'РР14',
'РР15',
'РР16',
'РР17',
'РР18',
'РР19',
'РР20',
'РР21',
'РР22',
'РР23',
'РР24',
'РР25',
'РР26',
'РР27',
'РР28',
'РР29',
'РР30',
'РР31',
'РР32',
'РР33',
'РР34',
'РР35',
'РР36',
'РР37',
'РР38',
'РР39',
'РР40',
'РР41',
'РР42',
'РР43',
'РР44',
'РР45',
'РР46',
'РР47',
'РР48',
'РР49',
'РР50',
'РР51',
'РР52',
'РР53',
'РР54',
'РР55',
'РР56',
'РР57',
'РР58',
'РР59',
'РР60',
'РР61',
'РР62',
'РР63',
'РР64',
'РР65',
'РР66',
'РР67',
'РР68',
'РР69',
'РР70',
'РР71',
'РР72',
'РР73',
'РР74',
'РР75',
'РР76',
'РР77',
'РР78',
'РР79',
'РР80',
'РР81',
'РР82',
'РР83',
'РР84',
'РР85',
'РР86',
'РР87',
'РР88',
'РР89',
'РР90',
'РР91',
'РР92',
'РР93',
'РР94',
'РР95',
'РР96',
'РР97',
'РР98',
'РР99',
'РР100'
]

# Составление таблицы с порядковым номером, обозначением, наименованием документа
documents_count = len(file_names)
output_data = []
for index in range(0, documents_count):
    # Разделение имени файла на обозначение и наименование
    file_name = os.path.splitext(file_names[index])[0]
    values = file_name.split()
    if values[1] in doc_codes:
        part_number = values[0] + ' ' + values[1]
        part_title = ' '.join(values[2:])
    else:
        part_number = values[0]
        part_title = ' '.join(values[1:])
    output_data.append([str(index + 1), part_number, part_title])

# Запись данных в файл в виде таблицы
document = Document()
table = document.add_table(rows=1, cols=3, style='Table Grid')
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
