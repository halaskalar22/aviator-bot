import os
import sys
import telebot
import traceback
from flask import Flask, request

TOKEN = "8770467906:AAGSR4BWwW6FT-kXyJrg3JAtK54Xk5jr1Pc"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        print("GELEN GÜNCELLEME:", data)
        sys.stdout.flush()
        
        if 'message' in data:
            message = data['message']
            chat_id = message['chat']['id']
            text = message.get('text', '')
            
            if text == '/start':
                print(">>> /start komutu manuel olarak yakalandı!")
                sys.stdout.flush()
                
                text_msg = (
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
                
                bot.send_message(chat_id, text_msg, reply_markup=markup)
                print(">>> Mesaj kullanıcıya başarıyla gönderildi!")
                sys.stdout.flush()
                
        return "OK", 200
    except Exception as e:
        print("WEBHOOK HATASI:", traceback.format_exc())
        sys.stdout.flush()
        return "Error", 500

@app.route('/')
def index():
    return "Bot aktif ve çalışıyor kanka!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))