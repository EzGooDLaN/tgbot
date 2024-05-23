import telebot
from telebot import types
import random
import webbrowser
import sqlite3

conn = sqlite3.connect('database.db')                                                                   # Подключение к базе данных
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS test_table (id INTEGER PRIMARY KEY, name TEXT)''')
conn.commit()


def get_data_from_db():                                                                                 # Выполнить запрос к базе данных
    cursor.execute("SELECT * FROM test_table")
    return cursor.fetchall()


conn.close()                                                                                            # Закрытие соединения с базой данных


bot = telebot.TeleBot('6882143733:AAEYiEZN92ttFRjmAtKzfE3r9sF2JFS_Rqc')                                 # Ввод токена

answers = ['Я не понял, что ты хочешь сказать.',
           'Извини, я тебя не понимаю.',                                                                # Примеры ответов бота на неизвестные команды
           'Я не знаю такой команды.']


@bot.message_handler(commands=['start', 'main', 'hello'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Товары')                                                         # Создание кнопок на главном меню
    button2 = types.KeyboardButton('📄 Справка')
    markup.row(button1)
    markup.row(button2)

    if message.text == '/start':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\n'
                                          f'У меня ты сможешь купить товары спортивного питания!\n'
                                          f'Контакт моего разработчика: https://t.me/EzGooDLaN', reply_markup=markup)       # Приветствие
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!', reply_markup=markup)


@bot.message_handler(content_types='photo')
def get_photo(message):                                                                     # Обработка фото.
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото.')    # Если пользователь пришлет фото, то бот отреагирует на него.


@bot.message_handler()
def info(message):
    if message.text == '🛍 Товары':
        catalogChapter(message)                                                            # Обработка обычных текстовых команд, описанных в кнопках
    elif message.text == '📄 Справка':
        infoChapter(message)
    elif message.text == '🔹Гейнеры':
        gainerChapter(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад')
        markup.row(button1)
    elif message.text == '🔹Протеин':
        proteinChapter(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад')
        markup.row(button1)
    elif message.text == '🔹BCAA':
        bcaaChapter(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад')
        markup.row(button1)
    elif message.text == '🔹Протеиновые батончики':
        proteinbarChapter(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад')
        markup.row(button1)
    elif message.text == 'PRIMEKRAFT Micellar Casein':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton('↩️ Назад')
        button1 = types.KeyboardButton('💳 Купить')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Мицеллярный казеин PRIMEKRAFT Micellar Casein Молочный шоколад, 900 гр / 30 порций\n'      # Товары
                                          'За одну порцию: 22 белки, 1 жиры, 2,5 углеводы, 104 ккал.\n'
                                          'Цена: 1800 рублей.', reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://ir.ozone.ru/s3/multimedia-f/wc1000/6665421579.jpg')
    elif message.text == 'Soul Way protein':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton('↩️ Назад')
        button1 = types.KeyboardButton('💳 Купить')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Комбо набор Протеин сыворотчный банановый 900 гр 30 порций + Креатин моногидрат '
                                          'без вкуса 300 гр 60 порций + Витамин С 60 капсул.\n'
                                          'За одну порцию: 20 белки, 1 жиры, 6,6 углеводы, 113.2 ккал.\n'
                                          'Цена: 1500 рублей.', reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://ir.ozone.ru/s3/multimedia-e/wc1000/6900337886.jpg')
    elif message.text == 'RusLabnutrition protein':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton('↩️ Назад')
        button1 = types.KeyboardButton('💳 Купить')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Протеин сывороточный ,белковый коктейль (800 гр),вкус ванильное мороженое, 25 порций.\n'
                                          'За одну порцию: 13 белки, 0,9 жиры, 13 углеводы, 108 ккал.\n'
                                          'Цена: 1000 рублей.', reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://ir.ozone.ru/s3/multimedia-j/wc1000/6211059703.jpg')
    elif message.text == 'Bombbar Whey Protein Pro':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton('↩️ Назад')
        button1 = types.KeyboardButton('💳 Купить')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Bombbar Протеин сывороточный без сахара Whey Protein Pro "Фисташковое мороженое", 900г/30 порций.\n'
                                          'За одну порцию: 21,3 белки, 2,8 жиры, 1,6 углеводы, 117 ккал.'
                                          'Цена: 1700 рублей.', reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://ir.ozone.ru/s3/multimedia-v/wc1000/6805362163.jpg')
    elif message.text == 'PRIMEKRAFT MASS gainer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton('↩️ Назад')
        button1 = types.KeyboardButton('💳 Купить')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Гейнер PRIMEKRAFT MASS GAINER для набора массы Шоколад 3000 гр / 30 порций / Дой-пак\n'
                                          'В одной порции: 14 белки, 0,75 жиры, 79 углеводы, 379 ккал.\n'
                                          'Цена: 2000 рублей.', reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://ir.ozone.ru/s3/multimedia-1-t/wc1000/6953430845.jpg')
    elif message.text == 'I.G. FIT gainer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton('↩️ Назад')
        button1 = types.KeyboardButton('💳 Купить')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Гейнер I.G. FIT на сложных (медленных) углеводах со вкусом орео, '
                                          '1000г (спортивное питание, гейнер для набора мышечной массы и веса с мерной ложкой)\n'
                                          'За одну порцию: 15 белки, 2,7 жиры, 67 углеводы, 370 ккал.\n'
                                          'Цена: 1100 рублей.', reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://ir.ozone.ru/s3/multimedia-1-y/wc1000/6913059838.jpg')
    elif message.text == 'TURBO MASS gainer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton('↩️ Назад')
        button1 = types.KeyboardButton('💳 Купить')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Гейнер TURBO MASS GAINER, шоколад, 1400 г. '
                                          'для набора мышечной массы белково-углеводный с витаминами / спортивное питание\n'
                                          'В одной порции: 10 белки, 2 жиры, 80 углеводы, 380 ккал.\n'
                                          'Цена: 800 рублей.', reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://ir.ozone.ru/s3/multimedia-u/wc1000/6148682154.jpg')
    elif message.text == 'BIGSNT gainer':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton('↩️ Назад')
        button1 = types.KeyboardButton('💳 Купить')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Гейнер BIGSNT BIG GAINER для набора мышечной массы высокобелковый, '
                                          'со вкусом мороженого / спортивное питание, 1.5 кг\n'
                                          'В одной порции: 43,4 белки, 9 жиры, 74 углеводы, 550 ккал.'
                                          'Цена: 1500 рублей.', reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://ir.ozone.ru/s3/multimedia-1-i/wc1000/7001881290.jpg')
    elif message.text == 'Bombbar proteinbar':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton('↩️ Назад')
        button1 = types.KeyboardButton('💳 Купить')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Bombbar Протеиновые батончики в шоколаде без сахара '
                                          '"Фисташковая меренга", 12шт х 40г\n'
                                          'В одной порции: 10 белки, 7 жиры, 2,5 углеводы, 142 ккал.\n'
                                          'Цена: 800 рублей.', reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://ir.ozone.ru/s3/multimedia-q/wc1000/6192069278.jpg')
    elif message.text == 'Bombbar proteinbar2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton('↩️ Назад')
        button1 = types.KeyboardButton('💳 Купить')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'Bombbar протеиновые батончики без сахара АССОРТИ №2, 20шт х 60г.\n'
                                          'В одной порции: 10 белки, 7 жиры, 2,5 углеводы, 142 ккал\n'
                                          'Цена: 1253 рублей.', reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://ir.ozone.ru/s3/multimedia-y/wc1000/6423489634.jpg')
    elif message.text == 'BIGSNT BCAA':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton('↩️ Назад')
        button1 = types.KeyboardButton('💳 Купить')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, 'BCAA 2:1:1 BIGSNT спортивное питание / комплекс незаменимых аминокислот для роста мышц,'
                                          ' порошок, 400 г (80 порций), вкус Малина.\n'
                                          'Цель: Восстановление, Выносливость, Красота и здоровье, Набор мышечной массы,'
                                          ' Повышение работоспособности, Похудение/Сушка, Профилактика, Сила\n'
                                          'Цена: 1182 рублей.', reply_markup=markup)
        bot.send_photo(message.chat.id, photo='https://ir.ozone.ru/s3/multimedia-v/wc1000/6425225263.jpg')
    elif message.text == '💳 Купить' or message.text == '✏️ Написать разработчику':                     # При покупке перекидывание в личные сообщения
        webbrowser.open('https://t.me/EzGooDLaN')
    elif message.text == '↩️ Назад':
        catalogChapter(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])                           # Рандомные ответы на неизвестные запросы


def catalogChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹Гейнеры')                                                          # Функция, отвечающая за раздел каталога
    button2 = types.KeyboardButton('🔹Протеин')
    button3 = types.KeyboardButton('🔹BCAA')
    button4 = types.KeyboardButton('🔹Протеиновые батончики')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)
    bot.send_message(message.chat.id, 'Вот все товары, которые сейчас находятся в продаже:', reply_markup=markup)


def proteinChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('PRIMEKRAFT Micellar Casein')
    button2 = types.KeyboardButton('Soul Way protein')                                                    # Функция, отвечающая за раздел товара
    button3 = types.KeyboardButton('RusLabnutrition protein')
    button4 = types.KeyboardButton('Bombbar Whey Protein Pro')
    button5 = types.KeyboardButton('↩️ Назад')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)
    bot.send_message(message.chat.id, 'Информация о протеине:', reply_markup=markup)


def gainerChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('PRIMEKRAFT MASS gainer')                                              # Функция, отвечающая за раздел товара
    button2 = types.KeyboardButton('I.G. FIT gainer')
    button3 = types.KeyboardButton('TURBO MASS gainer')
    button4 = types.KeyboardButton('BIGSNT gainer')
    button5 = types.KeyboardButton('↩️ Назад')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)
    bot.send_message(message.chat.id, 'Информация о гейнере:', reply_markup=markup)


def proteinbarChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)                                              # Функция, отвечающая за раздел товара
    button1 = types.KeyboardButton('Bombbar proteinbar')
    button2 = types.KeyboardButton('Bombbar proteinbar2')
    button3 = types.KeyboardButton('↩️ Назад')
    markup.row(button1, button2)
    markup.row(button3)
    bot.send_message(message.chat.id, 'Информация о батончиках:', reply_markup=markup)


def bcaaChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)                                              # Функция, отвечающая за раздел товара
    button1 = types.KeyboardButton('BIGSNT BCAA')
    button2 = types.KeyboardButton('↩️ Назад')
    markup.row(button1)
    markup.row(button2)
    bot.send_message(message.chat.id, 'Информация о BCAA:', reply_markup=markup)


def infoChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('✏️ Написать разработчику')                                            # Функция, отвечающая за раздел справки
    button2 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, 'Раздел справки.\n'
                                      'Здесь ты можешь написать моему разработчику.', reply_markup=markup)


bot.polling(none_stop=True)                                                                               # Бесконечная работа бота
