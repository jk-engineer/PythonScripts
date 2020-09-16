# Программа для скачивания демо-версии книги "Математика с ключом 6 класс. Часть 2".
# https://flipbook.nowaera.pl/dokumenty/Flipbook/Matematyka-z-kluczem[PD][cz_2][kl_6][pr_2019]
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


# Для корректной работы требуется:
#   Python версии 3.6 или выше
#   Установленные пакеты BeautifulSoup4, requests


import sys
import WebScraper


ws = WebScraper.WebScraper()
main_url = 'https://flipbook.nowaera.pl/dokumenty/Flipbook/Matematyka-z-kluczem[PD][cz_2][kl_6][pr_2019]/files/mobile/'
for index in range(1, 45):
    file_name = f'{index:02d}' + '.jpg'
    url = main_url + str(index) + '.jpg'
    ws.download_file(url, file_name)
    print(file_name)
print('Загрузка завершена.')
