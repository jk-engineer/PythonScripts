# Программа для удаления предыдущих версий документов PDF.
# Файлы должны иметь, например, следующие имена:
#    document.pdf
#    document_2020-10-26.pdf
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
from os import listdir
from os.path import isfile, join
import sys


def get_document_name(file_name: str, file_extension: str, separator: str):
    return file_name.replace(file_extension, '').split(separator)[0]


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

# Поиск дублирующихся файлов
current_name = ''
duplicates = []
output_data = []
separator = '_'
for name in file_names:
    if name in duplicates:
        continue
    file_extension = os.path.splitext(name)[1]
    current_name = get_document_name(name, file_extension, separator)
    duplicates = [f_name for f_name in file_names if get_document_name(f_name, file_extension, separator) == current_name]
    # При наличии нескольких файлов с одинаковыми начальными частями в имени дубликаты с более ранней датой изменения удаляются
    if len(duplicates) > 1:
        m_dates = [os.path.getmtime(f_name) for f_name in duplicates]
        max_date = max(m_dates)
        latest_file_name = duplicates[m_dates.index(max_date)]
        # Удаление старых версий файлов
        for del_name in duplicates:
            if del_name == latest_file_name:
                continue
            output_data.append(del_name)
            os.remove(del_name)

# Вывод имен удаленных файлов
print(f'\nУдалены файлы ({str(len(output_data))}):\n\n')
print('\n'.join(output_data))
