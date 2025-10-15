from fastapi import FastAPI, Request
from bot import dp, bot
from aiogram import executor
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # запускаем Telegram-бота при старте сервера
    loop = asyncio.get_event_loop()
    loop.create_task(executor.start_polling(dp, skip_updates=True))

@app.post("/avito-webhook")
async def avito_webhook(req: Request):
    data = await req.json()
    # пример: отправка сообщения одному пользователю
    await bot.send_message(123456789, f"Новое событие: {data}")
    return {"ok": True}
