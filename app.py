import os
import telebot
import traceback
from flask import Flask, request

TOKEN = "8770467906:AAGSR4BWwW6FT-kXyJrg3JAtK54Xk5jr1Pc"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    except Exception as e:
        print("HATA OLUŞTU:", traceback.format_exc())
        return "Error", 500

@app.route('/')
def index():
    return "Bot aktif ve çalışıyor kanka!", 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "🔥 AVİATOR ÖZEL YAZILIM & HİLE SİSTEMİ 🔥\n\n"
        "⚡ Kayıp Devrine Son! En güncel oran analizleri, gizli sinyal taktikleri ve VIP yazılım güncellemeleri burada.\n\n"
        "📍 Resmi Kanal: @aviator_yazilim\n"
        "💬 7/24 Destek & Satış: @DarkjokerAviator\n\n"
        "👇 Hemen aşağıdaki butonlardan kanalımıza katılabilir veya bilgi alabilirsin!"
    )
    
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton("📢 Resmi Kanalımıza Katıl", url="https://t.me/aviator_yazilim")
    btn2 = telebot.types.InlineKeyboardButton("💬 7/24 Destek & Satış Hattı", url="https://t.me/DarkjokerAviator")
    markup.add(btn1)
    markup.add(btn2)
    
    bot.send_message(message.chat.id, text, reply_markup=markup)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))