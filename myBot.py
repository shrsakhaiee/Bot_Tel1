import telebot
import random
from telebot import types
from gtts import gTTS
import qrcode

bot = telebot.TeleBot("5052398789:AAEKaW430ZvlOqT1jn7RsZ2Mop9pwCc3cg4")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"سلام عشقم... به ربات من خوش اومدی❤" + message.from_user.first_name)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,"چیکار میتونم برات بکنم؟🤗")

    
@bot.message_handler(commands=['qrcode'])
def creat_qr(message):
    bot.send_message(message.chat.id, 'متن را وارد کن ')
    @bot.message_handler(content_types=['text'])
    def creat_qr(message):
        qrcode_image =  qrcode.make("message.text")
        qrcode_image.save('qrcode.png')
        photo = open('qrcode.png','rb')
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['NewGame'])
def send_welcome(message):
    bot.reply_to(message,"انتخاب کن یه عدد بین 1 تا 50 :")
rdm = random.randint(0,50)
@bot.message_handler(func= lambda m: True)
def echo(message):
    s = int(message.text)
    if rdm == s:
        bot.reply_to(message,'درست گفتی')
    elif s < rdm:
        bot.reply_to(message,'برو بالا')
    elif s > rdm:
        bot.reply_to(message,'برو پایین')

@bot.message_handler(commands =['voice'])
def send_m(message):
    bot.reply_to(message,"Enter your text in English")
@bot.message_handler(func= lambda m: True)
def teype(message):		
    myobj = gTTS(text = message.text, slow=False)
    myobj.save('file.mp3')
    voice = open('file.mp3', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands =['Age'])
def send_s(message):
    myname = message.from_user.first_name
    bot.reply_to(message,"سال تولد خود را به شمسی وارد کنید" + message.from_user.first_name)
@bot.message_handler(func= lambda m: True)
def echo(message):
    sal = int(message.text)
    Hal = 1401 - sal
    bot.reply_to(message,"الان سالته"+ message.from_user.first_name)



@bot.message_handler(commands=['fal'])
def send_welcome(message):
    fal_list =['به سفر خواهی رفت','به فنا خواهی رفت','موش موش به دیدارت میاد']
    fal = random.choice(fal_list)
    bot.reply_to(message, fal)

@bot.message_handler(func=lambda m: True)
def send_welcome(message):
    if message.text == "سلام":
      bot.reply_to(message,"علیکم السلام")  
    elif message.text =="خوبی؟":
        bot.reply_to(message,"مرسی عشقم تو خوبی؟😘")  
    elif message.text == "خوابم میاد":
        bot.reply_to(message,"😏خو چیکار کنم به ...")
    elif message.text == "دوست دارم":
        bot.reply_to(message,"😎وظیفته")
    elif message.text == "یه عکس بده ببینمت؟":
        
        photo = open('sisi.jpg','rb')
        bot.send_photo(message.chat.id, photo)

    else:
        bot.reply_to(message,"چی میگی بابا درست بگو بفهمم")


     

bot.infinity_polling()