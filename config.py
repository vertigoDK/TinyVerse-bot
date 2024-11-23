# Telegram Bot Configuration
BOT_TOKEN = ""  # Replace with your actual bot token
SESSION_ID = ""         # Replace with your actual session ID
TELEGRAM_ID = ""       # Replace with your actual Telegram ID

# Set to True if you want to send messages to Telegram, otherwise set to False
SEND_TO_TELEGRAM = True

# Time tolerance in seconds for random intervals between star collection requests
TOLERANCE_FROM = 300  # Minimum time (in seconds) between requests
TOLERANCE_TO = 1000   # Maximum time (in seconds) between requests

# Number of star collection requests before querying stats
STATS_PER_REQUEST = 2