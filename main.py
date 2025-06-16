from flask import Flask, request
import requests
from config import BOT_TOKEN, CHAT_ID

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Приложение Flask запущено и работает!"

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    name = data.get('name')
    phone = data.get('phone')
    message = data.get('message')

    text = f"📩 Новый заказ!\n\n👤 Имя: {name}\n📞 Телефон: {phone}\n📝 Сообщение: {message}"
    send_to_telegram(text)

    return {"status": "ok"}

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    app.run(debug=True)
