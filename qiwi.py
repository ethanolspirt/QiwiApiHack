from qiwi_api import Qiwi
from ip2geotools.databases.noncommercial import DbIpCity
from itertools import chain
import json
from SimpleQIWI import *
import colorama
from time import sleep
colorama.init(autoreset=True)

#COLORAMA!
print('\t   ',colorama.Fore.YELLOW+'____  _          _',colorama.Fore.GREEN+'                  _   _    _            _     ')
print('\t  ',colorama.Fore.YELLOW+'/ __ \(_)        (_)',colorama.Fore.GREEN+'     /\         (_) | |  | |          | |    ')
print('\t ',colorama.Fore.YELLOW+'| |  | |___      ___ ',colorama.Fore.GREEN+'    /  \   _ __  _  | |__| | __ _  ___| | __ ')
print('\t ',colorama.Fore.YELLOW+'| |  | | \ \ /\ / / |',colorama.Fore.GREEN+'   / /\ \ | ',colorama.Fore.GREEN+'_ \| | |  __  |/ _` |/ __| |/ / ')
print('\t ',colorama.Fore.YELLOW+'| |__| | |\ V  V /| |',colorama.Fore.GREEN+'  / ____ \| |_) | | | |  | | (_| | (__|   <  ')
print('\t  ',colorama.Fore.YELLOW+'\___\_\_| \_/\_/ |_|',colorama.Fore.GREEN+' /_/    \_\ .__/|_| |_|  |_|\__,_|\___|_|\_\ ')
print('\t                                ',colorama.Fore.GREEN+'| |                                ')
print('\t                                ',colorama.Fore.GREEN+'|_|                     ')
print(colorama.Fore.GREEN+'\t ============================')
print(colorama.Fore.GREEN+'\t Creator:  deniskrupina')
print(colorama.Fore.GREEN+'\t YouTube:  https://www.youtube.com/channel/UCXMHZLzkWdl0Hb33H1LQAsw')
print(colorama.Fore.GREEN+'\t Gmail:    krupinad8@gmail.com')
print(colorama.Fore.GREEN+'\t ============================\n')
with open("Token Qiwi.txt",'r') as token:
    token = token.read()
phone = ''
print(colorama.Fore.GREEN+"Используемый Qiwi API: ",token)
def main():
    try:
        print(colorama.Fore.GREEN+'\tДействия:','\n',colorama.Fore.YELLOW+'[',colorama.Fore.RED+'1',colorama.Fore.YELLOW+']',colorama.Fore.GREEN+'Получить баланс\n',colorama.Fore.YELLOW+'[',colorama.Fore.RED+'2',colorama.Fore.YELLOW+']',colorama.Fore.GREEN+'Перевести деньги на кошелёк QIWI\n',colorama.Fore.YELLOW+'[',colorama.Fore.RED+'3',colorama.Fore.YELLOW+']',colorama.Fore.GREEN+'Получить данные о профиле\n',colorama.Fore.YELLOW+'[',colorama.Fore.RED+'4',colorama.Fore.YELLOW+']',colorama.Fore.GREEN+'Получить историю транзакций\n',colorama.Fore.YELLOW+'[',colorama.Fore.RED+'5',colorama.Fore.YELLOW+']',colorama.Fore.GREEN+'Узнать IP и местоположение\n')
        print(colorama.Fore.GREEN+">",end='')
        command = int(input())
        if command == 1:
            api = QApi(token=token,phone=phone)
            balance = api.balance
            print(colorama.Fore.GREEN+"Баланс: ",balance)
        elif command == 2:
            print(colorama.Fore.GREEN+"Ваш телефон: ",end='')
            phone1 = input()
            print(colorama.Fore.GREEN+"Телефон получателя: ",end='')
            phone2 = input()
            print(colorama.Fore.GREEN+"Сумма перевода: ",end='')
            amount = input()
            print(colorama.Fore.GREEN+"Комментарий: ",end='')
            comment = input()
            api = QApi(token=token,phone=phone1)
            api.pay ( account=phone2, amount=amount, comment=comment)
            print(colorama.Fore.GREEN+"Переведено!")
            sleep(1)
        elif command == 3:
            api = Qiwi(token)
            print(json.dumps(api.get_profile(), indent=1, sort_keys=True))
        elif command == 4:
            api = Qiwi(token)
            print(json.dumps(api.history(),sort_keys=True, indent=1))
        elif command == 5:
            api = Qiwi(token)
            x = api.get_profile()
            ipadress = x['authInfo']['ip']
            print(colorama.Fore.GREEN+'\nIP: ',ipadress)
            response = DbIpCity.get(ipadress, api_key='free')
            print(colorama.Fore.GREEN+"Город: ", response.city )
            print(colorama.Fore.GREEN+"Страна: ", response.country)
            print(colorama.Fore.GREEN+"Широта: ", response.latitude)
            print(colorama.Fore.GREEN+"Долгота: ", response.longitude )
            print(colorama.Fore.GREEN+"Регион: ", response.region)
        else:
            print(colorama.Fore.RED+"Действие не найдено!")
            sleep(2)
            
    except:
        print(colorama.Fore.RED+"\nОшибка!")
        sleep(1)
main()

while True:
    print(colorama.Fore.GREEN+"\nЖелаете выйти(y/n)?:",end='')
    ex1 = input()
    ex1.lower()
    if ex1 == 'n':
        main()
    elif ex1 == 'y':
        break
    else:
        break
