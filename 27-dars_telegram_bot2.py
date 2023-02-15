# 27- dars. kiril-lotin telegram bot

from transliterate import to_cyrillic, to_latin

import telebot
TOKEN="6001798060:AAH_DuGUHu9fIebpbbBseBDz_1tY1txacHw"
bot=telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    javob= "Assalomu alaykum. Xush kelibsiz !\n Matn kiriting : "
    bot.reply_to(message, javob)




@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    if msg.isascii():
        matn=to_cyrillic(msg)
    else:
        matn=to_latin(msg)        
        
    bot.reply_to(message, matn)

bot.infinity_polling()

print("Assalomu alaykum")


# matn=input("Matn kiriting : ")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))









