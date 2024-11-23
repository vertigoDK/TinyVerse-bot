from dotenv import load_dotenv

load_dotenv()

import os

# Telegram Bot Configuration
BOT_TOKEN = "your_telegram_bot_token"  # Replace with your actual bot token
SESSION_ID = "your_session_id"         # Replace with your actual session ID
TELEGRAM_ID = "your_telegram_id"       # Replace with your actual Telegram ID

# Set to True if you want to send messages to Telegram, otherwise set to False
SEND_TO_TELEGRAM = True

# Time tolerance in seconds for random intervals between star collection requests
TOLERANCE_FROM = 300  # Minimum time (in seconds) between requests
TOLERANCE_TO = 1000   # Maximum time (in seconds) between requests

STATS_PER_REQUEST = 10
