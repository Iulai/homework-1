"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Hi!')


def planet_constellation(update, context):
    planets_name = {
        'Mercury': ephem.Mercury(2021/11/25),
        'Venus': ephem.Venus(2021/11/25),
        'Mars': ephem.Mars(2021/11/25),
        'Jupiter': ephem.Jupiter(2021/11/25),
        'Saturn': ephem.Saturn(2021/11/25),
        'Uranus': ephem.Uranus(2021/11/25),
        'Neptune': ephem.Neptune(2021/11/25),
        'Pluto': ephem.Pluto(2021/11/25)
    }

    text = 'Вызван /planet'
    print(text)
    name = update.message.text.split(' ')[1]
    print(name)
    if name in planets_name:
        m = planets_name[name]
        const = ephem.constellation(m)
        print(const)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
