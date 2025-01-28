import asyncio
from telegram import Bot
from telegram.error import TelegramError

# Replace with your bot's token
TOKEN = '7519252602:AAE84WszNbopap4kgHf_zHtw-u630eu1Eb8'

# List of user IDs who will receive the "Hi" message
user_ids = [1487371960]  # Replace with actual user IDs



async def send_hi_message():
    bot = Bot(token=TOKEN)

    for user_id in user_ids:
        try:
            await bot.send_message(chat_id=user_id, text="Hi")
            print(f"Message sent to user {user_id}")
        except TelegramError as e:
            print(f"Error sending message to user {user_id}: {e}")


if __name__ == '__main__':
    asyncio.run(send_hi_message())
