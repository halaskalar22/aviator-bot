import os
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8770467906:AAFnvSEoS8A6FlCchOOJAsl5WhHeZ-4fOaU"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    btn_kanal = InlineKeyboardButton("📢 Resmi Kanalımıza Katıl", url="https://t.me/aviator_yazilim")
    btn_destek = InlineKeyboardButton("💬 7/24 Destek & Satış Hattı", url="https://t.me/DarkjokerAviator")
    markup.add(btn_kanal)
    markup.add(btn_destek)
    
    text = (
        "🔥 <b>AVİATOR ÖZEL YAZILIM & HİLE SİSTEMİ</b> 🔥\n\n"
        "⚡ <b>Kayıp Devrine Son! En güncel oran analizleri, gizli sinyal taktikleri ve VIP yazılım güncellemeleri burada.</b>\n\n"
        "📌 <b>Resmi Kanal:</b> @aviator_yazilim\n"
        "💬 <b>7/24 Destek & Satış:</b> @DarkjokerAviator\n\n"
        "👇 <b>Hemen aşağıdaki butonlardan kanalımıza katılabilir veya bilgi alabilirsin!</b>"
    )
    bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=markup)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route('/')
def index():
    return "Bot aktif ve çalışıyor kanka!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))