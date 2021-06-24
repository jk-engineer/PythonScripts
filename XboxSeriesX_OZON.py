# Программа для мониторинга наличия Xbox Series X в интернет-магазине ОЗОН


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
        results = [element.text for element in parsed_page.find_all('div') if element.get('class') is not None and 'kxa6' in element.get('class')]
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
