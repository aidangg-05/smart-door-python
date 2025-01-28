@echo off
echo Starting Telegram bot...
:loop
python telegramBot.py
echo Bot stopped. Restarting in 5 seconds...
timeout /t 5
goto loop