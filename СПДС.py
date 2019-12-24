# Данная программа скачивает стандарты СПДС с сайта Техэксперт.
# http://docs.cntd.ru/
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
main_url = 'http://docs.cntd.ru'
# Данные для входа в учетную запись
email = input('Введите адрес электронной почты\n')
password = input('Введите пароль\n')
login_data = {
    'return_url': '',
    'document': '',
    'holder': '',
    'email': email,
    'password': password
}

# Создание сессии, вход в учетную запись
login_url = 'http://docs.cntd.ru/user/login'
ws.session_object.get(login_url)
ws.session_object.post(login_url, data = login_data)

# Получение ссылок и названий документов
parsed_page = ws.page_parser_from_file('spds.html')
document_links = list(ws.get_attribute_values_by_element_value(parsed_page, 'a', 'href', 'Система проектной'))
document_names = list(ws.get_element_values(parsed_page, 'a', 'href', document_links))
document_names = [name.replace('\n', '') for name in document_names]
document_names = [name.replace('\t', '') for name in document_names]
document_names = [name.replace(':', '_') for name in document_names]
document_names = [name.replace('"', '') for name in document_names]
document_names = [name.replace('/', '_') for name in document_names]
document_names = [name.replace(' Система проектной документации для строительства (СПДС).', '') for name in document_names]
failed_downloads = []

# Загрузка документов
for index in range(0, len(document_links)):
    link = document_links[index]
    name = document_names[index]
    if len(name) > 101:
        name = name[:101]
    current_page = ws.page_parser(link)
    attribute_substring = link.replace(main_url + '/document', 'djvu')
    download_list = list(ws.get_attribute_values_by_attribute_value(current_page, 'a', 'href', 'href', attribute_substring))
    if len(download_list) > 0:
        download_url = main_url + download_list[0]
        ws.download_file(download_url, name + '.djvu')
        print('Загружен файл: ' + name)
    else:
        failed_downloads.append(name)

# Запись неудавшихся загрузок в файл
with open('spds_failed.txt', 'w', encoding = 'utf-8') as f_out:
    f_out.write('\n'.join(failed_downloads))

# Отчет о завершении работы
print('\n\nЗагрузка завершена')
