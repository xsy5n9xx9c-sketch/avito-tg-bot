from fastapi import FastAPI, Request
from bot import send_avito_message
from database import get_user
import json

app = FastAPI()

@app.post("/avito-webhook")
async def avito_webhook(req: Request):
    data = await req.json()
    print("Webhook data:", data)

    # Временный пример: отправка уведомления всем пользователям
    # Позже можно добавить фильтрацию по notify_types
    users = [get_user(uid) for uid in range(1, 1000)]  # пример, замените на реальную логику
    for user in users:
        if user:
            telegram_id = user[0]
            await send_avito_message(telegram_id, f"Новое событие: {json.dumps(data)}")
    return {"ok": True}
