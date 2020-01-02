# Программа скачивает документы НП "ОПЖТ" с официального сайта (раздел "Метрология"):
# http://opzt.ru/category/tehnicheskoe-regulirovanie/metrologiya/
# Copyright (C) 2019 Evgeniy Ipatov

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
#   Python версии 3.x
#   Установленные пакеты BeautifulSoup4, requests

import os
import WebScraper


main_url = 'http://opzt.ru'
documents_url = main_url + '/category/tehnicheskoe-regulirovanie/metrologiya/'
ws = WebScraper.WebScraper()
parsed_page = ws.page_parser(documents_url)
# Ссылки на документы
document_links = [link for link in ws.get_attribute_values(parsed_page, 'a', 'href')
                  if str(link).count('document') > 0]
# Имена документов
document_names = list(ws.get_element_values(parsed_page, 'a', 'href', document_links))
# Имена файлов (применено ограничение длины имени)
file_names = []
filename = ''
file_extension = ''
for doc_num in range(0, len(document_names)):
    filename = str(document_names[doc_num]).capitalize()
    if len(filename) > 100:
        filename = filename[:90] + '...'
    file_extension = os.path.splitext(document_links[doc_num])[1]
    file_names.append(filename + file_extension)
# Скачивание документов
download_doc_counter = 0
for doc_num in range(0, len(document_links)):
    ws.download_file(main_url + document_links[doc_num], file_names[doc_num])
    download_doc_counter += 1
    print('Загружено файлов: ' + str(download_doc_counter))
print('Загрузка файлов завершена')
