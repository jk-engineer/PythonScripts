# Программа для перемещения в резервную папку предыдущих версий документов PDF.
# Файлы должны иметь, например, следующие имена:
#    document.pdf
#    document_2020-10-26.pdf
# Copyright (C) 2020 - 2021 Evgeniy Ipatov

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


def get_document_name(file_name: str, file_extension: str, separator: str):
    return file_name.replace(file_extension, '').split(separator)[0]


# Выбор файлов с расширением pdf
p = pathlib.Path('.').glob('*.pdf')
file_names = sorted([name for name in p if name.is_file()])

# Выход из программы при отсутствии файлов pdf
if len(file_names) == 0:
    print('\nНе найдены файлы pdf. Завершение работы программы')
    sys.exit()

# Создание резервной папки для старых версий файлов
if pathlib.Path('Замененные').exists():
    old_files_folder_name = 'Замененные'
elif pathlib.Path('Заменённые').exists():
    old_files_folder_name = 'Заменённые'
else:
    pathlib.Path('Замененные').mkdir()
    old_files_folder_name = 'Замененные'

# Поиск дублирующихся файлов
current_name = ''
duplicates = []
output_data = []
separator = '_'
for name in file_names:
    if name in duplicates:
        continue
    file_extension = pathlib.Path(name).suffix
    current_name = get_document_name(str(name), file_extension, separator)
    duplicates = [f_name for f_name in file_names if get_document_name(str(f_name), file_extension, separator) == current_name]
    # При наличии нескольких файлов с одинаковыми начальными частями в имени дубликаты с более ранней датой изменения перемещаются в резервную папку
    if len(duplicates) > 1:
        m_dates = [f_name.stat().st_mtime for f_name in duplicates]
        max_date = max(m_dates)
        latest_file_name = duplicates[m_dates.index(max_date)]
        # Перемещение старых версий файлов в резервную папку
        for move_name in duplicates:
            if move_name == latest_file_name:
                continue
            output_data.append(str(move_name))
            new_name = pathlib.Path(old_files_folder_name) / move_name
            move_name.rename(new_name)

# Вывод имен перемещенных файлов
print(f'\nПеремещены файлы ({str(len(output_data))}):\n\n')
print('\n'.join(output_data))
