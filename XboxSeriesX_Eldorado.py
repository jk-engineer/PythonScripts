# Программа для мониторинга наличия Xbox Series X в интернет-магазине Эльдорадо


import random
import requests
import time
import webbrowser
import winsound

target_url = 'https://eldorado.ru/cat/detail/igrovaya-pristavka-microsoft-xbox-series-x/?utm_source=cms&utm_medium=email&utm_term=buy_button&utm_campaign=arrival_ready#addToCart'
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
