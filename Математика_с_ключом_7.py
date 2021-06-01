# Программа для скачивания книги "Математика с ключом 7 класс".
# https://flipbook.nowaera.pl/dokumenty/Flipbook/Matematyka-z-kluczem-7/
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


# Для корректной работы требуется:
#   Python версии 3.6 или выше
#   Установленные пакеты BeautifulSoup4, requests


import sys
import WebScraper


ws = WebScraper.WebScraper()
main_url = 'https://flipbook.nowaera.pl/dokumenty/Flipbook/Matematyka-z-kluczem-7/files/mobile/'
for index in range(1, 353):
    file_name = f'{index:03d}' + '.jpg'
    url = main_url + str(index) + '.jpg'
    ws.download_file(url, file_name)
    print(file_name)
print('Загрузка завершена.')
