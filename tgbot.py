import telebot
from telebot import types
import random
import webbrowser

bot = telebot.TeleBot('6882143733:AAEYiEZN92ttFRjmAtKzfE3r9sF2JFS_Rqc')

answers = ['Я не понял, что ты хочешь сказать.',
           'Извини, я тебя не понимаю.',
           'Я не знаю такой команды.',
           'Напиши нормально.']


@bot.message_handler(commands=['start', 'main', 'hello'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Товары')
    button2 = types.KeyboardButton('⚙️ Настройки')
    button3 = types.KeyboardButton('📄 Справка')

    markup.row(button1)
    markup.row(button2, button3)

    if message.text == '/start':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\n'
                                          f'У меня ты сможешь купить товары спортивного питания!\n'
                                          f'Контакт моего разработчика: https://t.me/EzGooDLaN', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!', reply_markup=markup)


@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')


@bot.message_handler()
def info(message):
    if message.text == '🛍 Товары':
        goodsChapter(message)
    elif message.text == '⚙️ Настройки':
        settingsChapter(message)
    elif message.text == '📄 Справка':
        infoChapter(message)
    elif message.text == '🔹 Товар #1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о первом товаре...', reply_markup=markup)
    elif message.text == '🔹 Товар #2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о втором товаре...', reply_markup=markup)
    elif message.text == '🔹 Товар #3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о третьем товаре...', reply_markup=markup)
    elif message.text == '🔹 Товар #4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Информация о четвертом товаре...', reply_markup=markup)
    elif message.text == '⚙️ Настройки #1':
        bot.send_message(message.chat.id, 'Настройки номер 1...')
    elif message.text == '⚙️ Настройки #2':
        bot.send_message(message.chat.id, 'Настройки номер 2...')
    elif message.text == '💳 Купить' or message.text == '✏️ Написать разработчику':
        webbrowser.open('https://t.me/EzGooDLaN')
    elif message.text == '↩️ Назад':
        goodsChapter(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])


def goodsChapter(message):
    # Кнопки для товаров
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 Товар #1')
    button2 = types.KeyboardButton('🔹 Товар #2')
    button3 = types.KeyboardButton('🔹 Товар #3')
    button4 = types.KeyboardButton('🔹 Товар #4')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)
    bot.send_message(message.chat.id, 'Вот все товары, которые сейчас находятся в продаже:', reply_markup=markup)


def settingsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('⚙️ Настройки #1')
    button2 = types.KeyboardButton('⚙️ Настройки #2')
    button3 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3)
    bot.send_message(message.chat.id, 'Раздел настроек.\n'
                                      'Выбери один из вариантов:', reply_markup=markup)


def infoChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('✏️ Написать разработчику')
    button2 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, 'Раздел справки.\n'
                                      'Здесь ты можешь написать моему разработчику.', reply_markup=markup)


bot.polling(none_stop=True)
