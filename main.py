import telebot
import requests
from telebot import types
import bs4
import time
import lxml
from bs4 import BeautifulSoup
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
bot= telebot.TeleBot("5018374776:AAFZKV1m-_wJf35XyN5wvqVtKD0MgsZVbpw")
@bot.message_handler(commands=["start"])
def keyboard_start(massage):
  startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
  Start = types.KeyboardButton(text= "Начать отслеживать погоду")
  Stop = types.KeyboardButton(text= "Прекратить отслеживать погоду")
  startKBoard.add(Start , Stop)
  bot.send_message(massage.chat.id, "Если хотите отслеживать погоду нажмите: Начать отслеживать погоду" , reply_markup=startKBoard)
@bot.message_handler(func=lambda m: m.text == 'Начать отслеживать погоду')
def weater(message):
    bot.send_message(message.chat.id, "Вы начали отслеживать погоду.")
    global a
    a += 1
    while a>0:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        b = "10:20:00"
        if current_time == b:
           headers = {
                   "User.agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.4.730 Yowser/2.5 Safari/537.36"
            }
           soup = BeautifulSoup(requests.get("https://weather.rambler.ru/v-kovrove/today/", headers=headers).text,
                                  "lxml")
           weather = soup.find(class_="ScUc").text
           bot.send_message(message.chat.id, weather)
        else:
            pass
a=0
@bot.message_handler(func= lambda m: m.text == "Прекратить отслеживать погоду")
def Stop(message):
    bot.send_message(message.chat.id, "Вы прекратили отслеживать погоду.")
    global a
    a = 0
bot.polling()