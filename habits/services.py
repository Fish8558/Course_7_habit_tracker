import requests
from config.settings import TELEGRAM_API_KEY

send_message_url = f'https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage'


def send_telegram_message(habit):
    """Отправка сообщения в Telegram"""
    user = habit.user
    message = create_message(habit, user)
    requests.post(
        url=send_message_url,
        data={
            'chat_id': user.telegram_chat_id,
            'text': message
        })


def create_message(habit, user):
    """Создание сообщения"""
    msg = (f"Привет, {user.name}! \n"
           f"Сегодня в {habit.time} в {habit.place} выполните действие \"{habit.action}\" "
           f"в течении {habit.duration_time} секунд! \nУдачи!!!")
    return msg
