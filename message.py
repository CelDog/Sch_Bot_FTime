import telebot

from telebot import types
 
bot = telebot.TeleBot('1228580983:AAE263fN6V5Ef-qGQ4iUs2rATQqpxWU7GXA')
        


@bot.message_handler(commands=['start'])
def welcome(message):
   
  
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Расписание уроков.")
    item2 = types.KeyboardButton("Расписание звонков.")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помочь тебе с расписанием.".format(message.from_user, bot.get_me()),
         reply_markup=markup)



@bot.message_handler(commands =['getadmin'])
def adminactive(message):
    bot.send_message(message.chat.id, "Для подтверждения введите пароль")
   
@bot.message_handler(content_types=['text'])
def an(message):
    if message.chat.type == 'private':
 
        if message.text == 'Расписание уроков.' or 'Вывести содержимое файлов':

        
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("1-А", callback_data='1-А')
            item2 = types.InlineKeyboardButton("1-Б", callback_data='1-Б')
            item3 = types.InlineKeyboardButton("2-А", callback_data='2-А')
            item4 = types.InlineKeyboardButton("2-Б", callback_data='2-Б')
            item5 = types.InlineKeyboardButton("3-А", callback_data='3-А')
            item6 = types.InlineKeyboardButton("3-Б", callback_data='3-Б')
            item7 = types.InlineKeyboardButton("4-А", callback_data='4-А')
            item8 = types.InlineKeyboardButton("4-Б", callback_data='4-Б')
            item9 = types.InlineKeyboardButton("5-А", callback_data='5-А')
            item10 = types.InlineKeyboardButton("5-Б", callback_data='5-Б')
            item11 = types.InlineKeyboardButton("6-А", callback_data='6-А')
            item12 = types.InlineKeyboardButton("6-Б", callback_data='6-Б')
            item13 = types.InlineKeyboardButton("7-А", callback_data='7-А')
            item14 = types.InlineKeyboardButton("7-Б", callback_data='7-Б')
            item15 = types.InlineKeyboardButton("8-А", callback_data='8-А')
            item16 = types.InlineKeyboardButton("8-Б", callback_data='8-Б')
            item17 = types.InlineKeyboardButton("9-А", callback_data='9-А')
            item18 = types.InlineKeyboardButton("9-Б", callback_data='9-Б')
            item19 = types.InlineKeyboardButton("10-А", callback_data='10-А')
            item20 = types.InlineKeyboardButton("10-Б", callback_data='10-Б')
            item21 = types.InlineKeyboardButton("11-А", callback_data='11-А')
            item22 = types.InlineKeyboardButton("11-Б", callback_data='11-Б')
            

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, item22)
 
            bot.send_message(message.chat.id, 'Выберите класс:', reply_markup=markup)
            
        elif message.text == 'Расписание звонков.':
 
            markup = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("1-ый класс", callback_data='1-1')
            item2 = types.InlineKeyboardButton("2-4-ый класс", callback_data='2-4')
            item3 = types.InlineKeyboardButton("5-11-ый класс", callback_data='5-11')
 
            markup.add(item1, item2, item3)
 
            bot.send_message(message.chat.id, 'Выберите класс:', reply_markup=markup)

        elif message.text == '003':
            bot.send_message(message.chat.id, "Режим администратора активен. Дальнейшие действия?(Если забыли выберите из списка(Для активации введите: 'Подсказка')")
        
        elif message.text == 'Подсказка':
            bot.send_message(message.chat.id, "Вывести содержимое файлов, Режим редактирования")

        else:
            bot.send_message(message.chat.id, 'Извините, меня не научили отвечать на такие сообщения.')

def changemod(message):
    bot.send_message(message.chat.id, "Расписание уроков, Изменение файла")
    an(message)
    callback_inline(message)
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '1-1':
                bot.send_message(call.message.chat.id, '1. 8.00-8.35\n2. 8.55-9.30\n3. 9.50-10.25\n4. 10.45-11.20\n5. 11.45-12.20\n6. 12.40-13.15')
            elif call.data == '2-4':
                bot.send_message(call.message.chat.id, '1. 8.00-8.40\n2. 8.55-9.35\n3. 9.50-10.30\n4. 10.45-11.25\n5. 11.45-12.25\n6. 12.40-13.15\n7. 13.35-14.15\n8. 14.30-15.10\n9. 15.20-16.00')
            elif call.data == '5-11':
                bot.send_message(call.message.chat.id, '1. 8.00-8.45\n2. 8.55-9.40\n3. 9.50-10.35\n4. 10.45-11.30\n5. 11.45-12.30\n6. 12.40-13.25\n7. 13.35-14.20\n8. 14.30-15.15\n9. 15.20-16.05')
            elif call.data == '10-А':
                less = open('10-A.txt','rt')
                bot.send_message(call.message.chat.id, less.read())
            elif call.data == '1-А':
                less1 = open('1-А.txt','rt')
                bot.send_message(call.message.chat.id, less1.read())
            elif call.data == '1-Б':
                less2 = open('1-Б.txt', 'rt')
                bot.send_message(call.message.chat.id, less2.read())
            elif call.data == '2-А':
                less3 = open('2-А.txt', 'rt')
                bot.send_message(call.message.chat.id, less3.read())
            elif call.data == '2-Б':
                less4 = open('2-Б.txt', 'rt')
                bot.send_message(call.message.chat.id, less4.read())
            elif call.data == '3-А':
                less5 = open('3-А.txt', 'rt')
                bot.send_message(call.message.chat.id, less5.read())
            elif call.data == '3-Б':
                less6 = open('3-Б.txt','rt')
                bot.send_message(call.message.chat.id, less6.read())
            elif call.data == '4-А':
                less7 = open('4-А.txt','rt')
                bot.send_message(call.message.chat.id, less7.read())
            elif call.data == '4-Б':
                less8 = open('4-Б.txt', 'rt')
                bot.send_message(call.message.chat.id, less8.read())
            elif call.data == '5-А':
                less9 = open('5-А.txt', 'rt')
                bot.send_message(call.message.chat.id, less9.read())
            elif call.data == '5-Б':
                less10 = open('5-Б.txt', 'rt')
                bot.send_message(call.message.chat.id, less10.read())
            elif call.data == '6-А':
                less11 = open('6-А.txt', 'rt')
                bot.send_message(call.message.chat.id, less11.read())
            elif call.data == '6-Б':
                less12 = open('6-Б.txt','rt')
                bot.send_message(call.message.chat.id, less12.read())
            elif call.data == '7-А':
                less13 = open('7-А.txt', 'rt')
                bot.send_message(call.message.chat.id, less13.read())
            elif call.data == '7-Б':
                less14 = open('7-Б.txt', 'rt')
                bot.send_message(call.message.chat.id, less14.read())
            elif call.data == '8-А':
                less15 = open('8-А.txt', 'rt')
                bot.send_message(call.message.chat.id, less15.read())
            elif call.data == '8-Б':
                less16 = open('8-Б.txt', 'rt')
                bot.send_message(call.message.chat.id, less16.read())
            elif call.data == '9-А':
                less17 = open('9-А.txt','rt')
                bot.send_message(call.message.chat.id, less17.read())
            elif call.data == '9-Б':
                less18 = open('9-Б.txt','rt')
                bot.send_message(call.message.chat.id, less18.read())
            elif call.data == '10-Б':
                less19 = open('10-Б.txt', 'rt')
                bot.send_message(call.message.chat.id, less19.read())
            elif call.data == '11-А':
                less20 = open('11-А.txt', 'rt')
                bot.send_message(call.message.chat.id, less20.read())
            elif call.data == '11-Б':
                less21 = open('11-Б.txt', 'rt')
                bot.send_message(call.message.chat.id, less21.read())
            
        
            
 
            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = 'Ответ:', reply_markup=None)
 
    except Exception as e:
        print(repr(e))
 
bot.polling(none_stop=True)