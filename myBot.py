import telebot
import random
from gtts import gTTS
import qrcode

bot = telebot.TeleBot("5052398789:AAEKaW430ZvlOqT1jn7RsZ2Mop9pwCc3cg4")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"سلام عشقم... به ربات من خوش اومدی❤" + message.from_user.first_name)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, """
    سلام به ربات من خوش اومدی
    جهت محاسبه سن → /age
    برای شروع بازی → /newgame
    برای دریافت فال → /fal
    برای تبدیل متن به کیوآر → /qr
    و برای تبدیل متن به صدا → /voice
    رو کلیک کن.""")


@bot.message_handler(commands=['qrcode'])
def creat_qr(message):
    qrcode = bot.send_message(message.chat.id, 'متن را وارد کن ')
    bot.register_next_step_handler(qrcode, sendqr)
def sendqr(message):
    qrcode_image =  qrcode.make("message.text")
    qrcode_image.save('qrcode.png')
    photo = open('qrcode.png','rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['newgame'])
def start_message(message):
  game = random.randint(1,30)
  game_message = bot.send_message(message.chat.id,"به بازی حدس عدد خوش اومدی، بین عدد 1 تا 30 حدس بزن")

  @bot.message_handler(func= lambda m: True)
  def guess(message):
    pc_num = int(message.text)
    if game == pc_num:
      bot.reply_to(message,'دمت گرم درست حدس زدی')
    elif pc_num < game:
      bot.reply_to(message,'برو بالا')
    elif pc_num > game:
      bot.reply_to(message,'بیا پایین')


@bot.message_handler(commands =['voice'])
def voice_s(message):
    javab = bot.send_message(message.chat.id,"Enter your text in English")
    bot.register_next_step_handler(javab, voice_send)
def voice_send(message):
    myobj = gTTS(text = message.text, slow=False)
    myobj.save('file.mp3')
    voice = open('file.mp3', 'rb')
    bot.send_voice(message.chat.id, voice)



@bot.message_handler(commands =['age'])
def send_age(message):
    pasokh = bot.send_message(message.chat.id,f"Enter the year that you born.")
    bot.register_next_step_handler(pasokh, sen)
def sen(message):
    year = int(message.text)
    now = 1401 - year
    bot.send_message(message.chat.id,f"You Are on {now} age.")


@bot.message_handler(commands=['fal'])
def fal_giri(message):
    fal = bot.send_message(message,"Mikham Falet begirom!")
    bot.register_next_step_handler(fal, matne_fal)
def matne_fal(message):
    fal_list =['به سفر خواهی رفت','به فنا خواهی رفت','موش موش به دیدارت میاد']
    fal = random.choice(fal_list)
    bot.reply_to(message, fal)


bot.infinity_polling()
