# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import asyncio
from telegram import Bot
from telegram.error import TelegramError

# Telegram Bot Token
TOKEN = '7519252602:AAE84WszNbopap4kgHf_zHtw-u630eu1Eb8'
user_ids = [1487371960, 1050472604]  # Replace with actual user IDs

# GPIO setup for ultrasonic sensor
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.OUT)  # GPIO25 as Trig
GPIO.setup(27, GPIO.IN)  # GPIO27 as Echo


# Function to measure distance
def measure_distance():
    # Produce a 10µs pulse at Trig
    GPIO.output(25, 1)
    time.sleep(0.00001)
    GPIO.output(25, 0)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(27) == 0:
        StartTime = time.time()  # Capture start of high pulse

    while GPIO.input(27) == 1:
        StopTime = time.time()  # Capture end of high pulse

    ElapsedTime = StopTime - StartTime
    Distance = (ElapsedTime * 34300) / 2  # Compute distance in cm
    return Distance


# Asynchronous function to send Telegram message
async def send_message():
    bot = Bot(token=TOKEN)
    for user_id in user_ids:
        try:
            print(f"Sending message to user {user_id}...")
            await bot.send_message(chat_id=user_id, text="Hi")
            print(f"Message sent to user {user_id}")
        except TelegramError as e:
            print(f"Error sending message to user {user_id}: {e}")


# Main loop to check distance and trigger Telegram message
async def monitor_distance():
    while True:
        distance = measure_distance()
        print(f"Measured distance: {distance:.1f} cm")

        if distance < 10:
            print("Distance < 10 cm! Sending message...")
            await send_message()
            print("Message sent. Waiting 5 seconds before resuming...")
            await asyncio.sleep(5)  # Pause before next check

        await asyncio.sleep(1)  # Check distance every 1 second


if __name__ == '__main__':
    print("Starting distance monitoring...")
    asyncio.run(monitor_distance())
