import sqlite3
import json
from config import DB_FILE

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    telegram_id INTEGER PRIMARY KEY,
                    avito_accounts TEXT,
                    notify_types TEXT
                )''')
    conn.commit()
    conn.close()

def add_user(telegram_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (telegram_id, avito_accounts, notify_types) VALUES (?, ?, ?)",
              (telegram_id, "[]", "all"))
    conn.commit()
    conn.close()

def update_user_accounts(telegram_id, accounts):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE users SET avito_accounts=? WHERE telegram_id=?", (accounts, telegram_id))
    conn.commit()
    conn.close()

def update_notify_type(telegram_id, notify_type):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("UPDATE users SET notify_types=? WHERE telegram_id=?", (notify_type, telegram_id))
    conn.commit()
    conn.close()

def get_user(telegram_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE telegram_id=?", (telegram_id,))
    row = c.fetchone()
    conn.close()
    return row
