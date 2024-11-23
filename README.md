# Script on python for Tiny Universe stars collection

This project provides a bot that collects star dust from a service using an API and sends updates to Telegram. You can configure it to run on a random interval and track your progress over time.

## Prerequisites

- Python 3.10+
- Required Python packages (listed below)

## Getting Started

Follow these steps to set up and use the bot:

### 1. Obtaining Your Session ID

To get your `SESSION_ID`, follow these steps:

1. Open your browser and go to telegram.web
2. Press `F12` to open the Developer Tools
3. Go to the `Network` tab
4. Trigger a star collection request (perform the action that collects stars)
5. Find the `POST` request named `collect` in the network logs
6. In the `Payload` section of the `collect` request, you will find the `session` field. This is your `SESSION_ID`

### 2. Finding Your Telegram ID

To find your `TELEGRAM_ID`, you can use telegram bot for example @getMyID_tgbot:

### 3. Configuring the `config.py` File

Create a `config.py` file to store the following settings:

```python
# Telegram Bot Configuration
BOT_TOKEN = "your_telegram_bot_token"  # Replace with your actual bot token
SESSION_ID = "your_session_id"         # Replace with your actual session ID
TELEGRAM_ID = "your_telegram_id"       # Replace with your actual Telegram ID

# Set to True if you want to send messages to Telegram, otherwise set to False
SEND_TO_TELEGRAM = True

# Time tolerance in seconds for random intervals between star collection requests
TOLERANCE_FROM = 300  # Minimum time (in seconds) between requests
TOLERANCE_TO = 3600   # Maximum time (in seconds) between requests

# Number of star collection requests before querying stats
STATS_PER_REQUEST = 2
```

Make sure to replace the placeholder values (`your_telegram_bot_token`, `your_session_id`, `your_telegram_id`) with your actual information.

### 4. Running the Bot

1. Install the necessary Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the bot:
   ```bash
   python main.py
   ```

The bot will start collecting stars at random intervals and send the updates to your Telegram account (if configured to do so).

## Disclaimer

By using this software, you agree that you are responsible for any actions performed with it. I do not accept any responsibility for any damage or consequences resulting from using this bot or its components. Use at your own risk.