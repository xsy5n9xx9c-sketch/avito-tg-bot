from aiogram import Bot, Dispatcher, types
import json
from database import init_db, add_user, update_user_accounts, update_notify_type, get_user
from avito_api import get_avito_token
from config import TELEGRAM_BOT_TOKEN

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

init_db()

@dp.message(commands=["start"])
async def start(msg: types.Message):
    add_user(msg.from_user.id)
    await msg.answer(
        "👋 Привет! Этот бот будет присылать уведомления с Avito.\n"
        "Используй /connect чтобы подключить свой аккаунт Avito.\n"
        "Используй /settings чтобы выбрать тип уведомлений."
    )

@dp.message(commands=["connect"])
async def connect(msg: types.Message):
    args = msg.get_args().split()
    if len(args) < 2:
        return await msg.answer("⚙️ Использование: /connect CLIENT_ID CLIENT_SECRET")
    client_id, client_secret = args
    token = get_avito_token(client_id, client_secret)
    if not token:
        return await msg.answer("❌ Ошибка авторизации в Avito.")
    user = get_user(msg.from_user.id)
    accounts = json.loads(user[1])
    accounts.append({'client_id': client_id, 'client_secret': client_secret})
    update_user_accounts(msg.from_user.id, json.dumps(accounts))
    await msg.answer("✅ Аккаунт Avito подключён!")

@dp.message(commands=["settings"])
async def settings(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("messages", "responses", "all")
    await msg.answer("Выберите тип уведомлений:", reply_markup=keyboard)

@dp.message(lambda message: message.text in ["messages", "responses", "all"])
async def set_notify_type(msg: types.Message):
    update_notify_type(msg.from_user.id, msg.text)
    await msg.answer(f"✅ Настройки уведомлений сохранены: {msg.text}")

async def send_avito_message(user_id, text):
    await bot.send_message(user_id, text)
