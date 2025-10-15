from fastapi import FastAPI, Request
import asyncio
from bot import dp, bot

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    # Запускаем Telegram-бота
    asyncio.create_task(dp.start_polling(bot))

@app.post("/avito-webhook")
async def avito_webhook(req: Request):
    data = await req.json()
    # пример: уведомление для одного пользователя (замени на логику для всех)
    await bot.send_message(123456789, f"Новое событие: {data}")
    return {"ok": True}
