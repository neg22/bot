import telebot
import requests
from bs4 import BeautifulSoup
import time
import random

bot = telebot.TeleBot('5496027166:AAEN80Mpt2y69jan241P5KLLoZmSeoPzsOY') #ключ индификатор

@bot.message_handler(content_types=["text"]) # принимает входящее сообщение 
def repeat_all_messages(message): # Название функции не играет никакой роли, приниает текст (может и доки и аудио) 
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, чтобы узнать какие команды есть напиши /help")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Пока нихуяшиньки нет 🫣")
    elif message.text == "/погода":
        print('каждые 10 минут обращаеться к сайту YandexПогода и считывает данные о погоде в данный момент ')
        print('')
        print('------')
        print('так определяется когда скоро будет дождь или идет !зависит от того как отрабатывает яндекс! и далее будет передаваться информация в бота для отправки в чат')
        print('------')
        print('')
        print('n:n:n В течение 30 минут дождь закончится - !этот формат показывает работает ли приложение!  ')
        print('')
        print('eсли показывает None это значит данные не пришли по какойто причине, либо отвалился нэт либо яндекс переименовал див на время - защита от ботов ')
        print('')

        while 1 == 1:
            url = "https://yandex.ru/pogoda/maps/nowcast?lat=57.62656&lon=39.893813&via=mmapw&le_Lightning=1&ll=39.893813_57.626560&z=9"
            yslovie = 'ясно. В ближайшие 2 часа осадков не ожидается'

            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'lxml')
            s = soup.find('div', class_='weather-maps-fact__nowcast-alert') #так сваливаемся до нужного места
            if s == None: # проверка на отсутствие двнных
                bot.send_message(message.from_user.id, s)
                print(s)
                time.sleep(60)
                continue
            s = s.text #так вытаскивать # бработать нул
            str(s)

            theFirstCondition = "ожидается"
            theSecondCondition = "дождь"
            arr = s.split() # из строки делает список
            x = len(arr)    # длинна списка
            count = 0
            ok  =   0       # флаг, если флаги сойдутся значит полное совпадение
            tfc =   0       # флаг 
            tsc =   0       # флаг

            while count < x:# пробежаться по списку
                if arr[count] == theFirstCondition:     #проверка на совпадение слова
                    tfc = 1
                if arr[count] == theSecondCondition:    #проверка на совпадение слова
                    tsc = 1
                count = count + 1
                if tfc == 1 & tsc == 1: #проверка на совпадения ключевых слов
                    ok = 1
            tfc = tsc = count = 0  #обнуление флагов счетчика
            
            if ok == 1: #условие на полное совпадение
                print('-----------------------------')
                #bot.send_message(message.from_user.id, "Есть полное совпадение")
                print("Есть полное совпадение")
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S ", t)
                bot.send_message(message.from_user.id, current_time + s + " Подробнее можно посмотреть тут https://yandex.ru/pogoda/maps/nowcast?lat=57.62656&lon=39.893813&via=mmapw&le_Lightning=1&ll=39.893813_57.626560&z=9")
                print(current_time + s)
                print('-----------------------------')
            else:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S ", t)
                print(current_time + s)
            ok = 0
                
            time.sleep(600)
            print('-')




if __name__ == '__main__':
    bot.infinity_polling()
