# Программа для мониторинга наличия Xbox Series X в интернет-магазине ОЗОН
# Copyright (C) 2021 Evgeniy Ipatov

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

from bs4 import BeautifulSoup as bSoup
import certifi
import random
import requests
import time
import webbrowser
import winsound


target_url = 'https://www.ozon.ru/product/igrovaya-konsol-microsoft-xbox-series-x-chernyy-173667655/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
exit_flag = False
session_object = requests.Session()

while True:
    print(time.strftime('%H:%M:%S', time.localtime()))
    for index in range(0, random.randint(5, 10)):
        ok_response = False
        while not ok_response:
            try:
                response = session_object.get(target_url, headers=headers, verify=certifi.where())
                ok_response = True
            except:
                session_object = requests.Session()
        parsed_page = bSoup(response.text, 'html.parser')
        results = [element.text for element in parsed_page.find_all('div', class_='kxa6')]
        if 'Добавить в корзину' in results:
            exit_flag = True
            break
        small_delay = random.randint(1, 10)
        time.sleep(small_delay)
    if exit_flag:
        break
    else:
        large_delay = random.randint(300, 600)
        time.sleep(large_delay)

print('\nGot it!')
webbrowser.open_new_tab(target_url)
for index in range(0, 100):
    winsound.Beep(800, 1000)
user_answer = input()
