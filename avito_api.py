import requests

def get_avito_token(client_id, client_secret):
    url = "https://api.avito.ru/token/"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    r = requests.post(url, data=data)
    if r.status_code == 200:
        return r.json()["access_token"]
    return None

# Здесь можно добавить функции для получения новых сообщений/событий
# и фильтрации по типам уведомлений
