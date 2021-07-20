# Программа для мониторинга наличия Xbox Series X в интернет-магазине Эльдорадо
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

import random
import requests
import time
import webbrowser
import winsound

target_url = 'https://eldorado.ru/cat/detail/igrovaya-pristavka-microsoft-xbox-series-x/?utm_source=cms&utm_medium=email&utm_term=sku_link&utm_campaign=arrival_ready'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
success_code = 200
exit_flag = False
session_object = requests.Session()

while True:
    print(time.strftime('%H:%M:%S', time.localtime()))
    for index in range(0, random.randint(5, 10)):
        request_result = session_object.get(target_url, headers=headers)
        if request_result.status_code == success_code:
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
