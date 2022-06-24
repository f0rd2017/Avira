import telebot
from config import *
import time
import pymysql
import pymysql.cursors
import datetime

bot = telebot.TeleBot(bot_key)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привіт {message.from_user.first_name}!')
    time.sleep(1)
    bot.send_message(message.chat.id, 'Відправ мені гаманець щоб отримати токени')
    time.sleep(1)
    bot.send_message(message.chat.id, 'Отримати їх можна 1 раз в день')

@bot.message_handler()
def get_adress(message):
    adress = message.text

    if (message.text == "Бот, будь-ласка дай гаманець🥺"):
        bot.send_message(message.chat.id, 'Тримай друже🥺')
        time.sleep(1)
        bot.send_message(message.chat.id, '0x12c7264e01dbb8bdf3ece238275aad847fb4c43013c45d149bf6e62a3505703d')
        return 0
    elif(len(adress) == 66):
        pass
    else:
        return 0


    result = ''
    bot.send_message(message.chat.id, 'Вже відправляю!')
    try:
        connection = pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=NAME,
            port=3306,
            cursorclass=pymysql.cursors.DictCursor)
    except Exception as ex:
        print('Ошибка подключения к базе данных ')
    try:

        with connection.cursor() as cursor:
            sql = f"SELECT `wallet`, `tap_lastDate` FROM `main_wallet` WHERE `wallet` = '{adress}'"
            cursor.execute(sql)
            result = cursor.fetchone()

        date_now = datetime.date.today()
        date = result['tap_lastDate']

        if(date != None):
            if (date_now <= date):
                time.sleep(1)
                bot.send_message(message.chat.id, 'Ви вже забрали бонус')
                return 0

        amount_avira = 0.0
        amount_tron = 0.0
        amount_usdt = 0.0

        with connection.cursor() as cursor:
            sql = f"SELECT `wallet`, `Tron`, `Avira`, `USDT` FROM `main_wallet` WHERE `wallet` = '{adress}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            amount_avira = float(result['Avira']) + float(get_amount / 2)
            amount_tron = float(result['Tron']) + float(get_amount)
            amount_usdt = float(result['USDT']) + float(get_amount / 5)
        connection.commit()

        with connection.cursor() as cursor:
            sql = f"UPDATE `AviraWallet`.`main_wallet` SET `Tron` = '{amount_tron}', `Avira` = '{amount_avira}', `USDT` = '{amount_usdt}', `tap_lastDate` = '{date_now.year}-{date_now.month}-{date_now.day}' WHERE (`wallet` = '{adress}');"
            cursor.execute(sql)
        connection.commit()
        time.sleep(1)
        bot.send_message(message.chat.id, 'Готово!')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Я відправив вам...')
        time.sleep(1)
        bot.send_message(message.chat.id, '10 Tron\n 5 Avira \n 2 USDT')
        time.sleep(1)
        bot.send_message(message.chat.id, u'\U00002764')

    finally:
        connection.close()



bot.polling(none_stop=True)
