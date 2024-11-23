from aiogram import Bot
import config
# Создаем объекты бота и диспетчера
bot = Bot(token=config.BOT_TOKEN)

# Метод notify для отправки сообщений
async def notify(user_id = config.TELEGRAM_ID, message: str = "ау"):
    """
    Отправляет сообщение пользователю с указанным user_id.
    :param user_id: Telegram ID пользователя
    :param message: Текст сообщения
    """
    try:
        await bot.send_message(chat_id=user_id, text=message)
    except Exception as e:
        print(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")
