# Программа скачивает набор иконок в формате PNG с сайта:
# http://www.iconarchive.com/show/oxygen-icons-by-oxygen-icons.org.1.html
# Copyright (C) 2019 Evgeniy Ipatov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import WebScraper


ws = WebScraper.WebScraper()
main_url = 'http://www.iconarchive.com/show/oxygen-icons-by-oxygen-icons.org.'
download_url = 'http://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/'
# Размеры иконок в пикселях
icon_sizes = [256, 128, 96, 72, 64, 48, 32, 24, 16]
error_files = []
for index in range(1, 19):
    parsed_page = ws.page_parser(main_url + str(index) + '.html')
    # Получение имен всех иконок на странице
    icon_names = list(ws.get_attribute_values_by_attribute_value(parsed_page, 'a', 'href', 'href', '-icon.html'))
    # Удаление дублирующихся имен
    icon_names = list(set(icon_names))
    for name in icon_names:
        icon_name = str(name).split('/')[-1]
        icon_name = icon_name.replace('.html', '.png')
        for size in icon_sizes:
            file_name = icon_name.replace('-icon', '_' + str(size) + 'x' + str(size))
            try:
                ws.download_file(download_url + str(size) + '/' + icon_name, file_name.lower())
            except:
                error_files.append(file_name)
            print(file_name)
print('Ошибка загрузки:')
print('\n'.join(error_files))
