import threading
import uvicorn
from bot import dp
from server import app
from aiogram import executor

def start_bot():
    executor.start_polling(dp, skip_updates=True)

def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    start_server()
