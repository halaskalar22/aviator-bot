import os
import telebot
from flask import Flask, request

TOKEN = "8770467906:AAFnvSEoS8A6FlCchOOJAsl5WhHeZ-4fOaU"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route('/')
def index():
    return "Bot aktif ve çalışıyor kanka!", 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "<b>🔥 AVİATOR ÖZEL YAZILIM & HİLE SİSTEMİ 🔥\n\n"
        "⚡ Kayıp Devrine Son! En güncel oran analizleri, gizli sinyal taktikleri ve VIP yazılım güncellemeleri burada.\n\n"
        "📍 Resmi Kanal: @aviator_yazilim\n"
        "💬 7/24 Destek & Satış: @DarkjokerAviator\n\n"
        "👇 Hemen aşağıdaki butonlardan kanalımıza katılabilir veya bilgi alabilirsin!</b>"
    )
    
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton("📢 Resmi Kanalımıza Katıl", url="https://t.me/aviator_yazilim")
    btn2 = telebot.types.InlineKeyboardButton("💬 7/24 Destek & Satış Hattı", url="https://t.me/DarkjokerAviator")
    markup.add(btn1)
    markup.add(btn2)
    
    bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=markup)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))