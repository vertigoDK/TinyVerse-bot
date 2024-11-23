import asyncio
from .API import APIHandler
from ..telegram_bot.telegram_service import notify
from ..tools.generate_random_between_range import generate_random_between_range
import config
import logging
import time


logging.basicConfig(level=logging.INFO)

class Bot:
    def __init__(self):
        self.tolerance_from: int = config.TOLERANCE_FROM
        self.tolerance_to: int = config.TOLERANCE_TO
        self.api_handler = APIHandler()
        self.stats_per_request = config.STATS_PER_REQUEST

    async def run(self):
        if config.SEND_TO_TELEGRAM:
            await notify(message="Bot started!")
        
        while True:
            try:
                await self._collect_stars()
                await self._handle_statistics()
                await self._attempt_auto_buy()
                
                # Random sleep interval
                time_to_collect = generate_random_between_range(self.tolerance_from, self.tolerance_to)
                await asyncio.sleep(time_to_collect)

            except Exception as e:
                logging.error(f"Error while processing: {e}", exc_info=True)
                await notify(message=f"Error while processing: {e}")

    async def _collect_stars(self):
        """Collect stars through the API and notify if successful."""
        response = self.api_handler.collect_stars()
        if response.get("response", {}).get("success") == 1:
            dust = response["response"]["dust"]
            logging.info(f"🌌 Successfully collected {dust} stardust.")
        else:
            logging.warning("Failed to collect stars.")

    async def _handle_statistics(self):
        """Send statistics update when required."""
        self.stats_per_request -= 1
        if self.stats_per_request == 0:
            response_stats = self.api_handler.check_stats()
            formatted_stats = self._format_stats(response_stats)
            
            if config.SEND_TO_TELEGRAM:
                await notify(message=formatted_stats)
            
            logging.info(formatted_stats)
            self.stats_per_request = config.STATS_PER_REQUEST

    async def _attempt_auto_buy(self):
        """Try to buy stars if the feature is enabled."""
        if config.STARS_AUTO_BUY:
            self.api_handler.buy_stars()

    def _format_stats(self, stats: dict) -> str:
        response = stats.get("response", {})
        return (
            f"📊 User Statistics\n\n"
            f"👤 General Information\n"
            f" - ID: {response.get('id')}\n"
            f" - Name: {response.get('first_name', '')} {response.get('last_name', '')}\n"
            f" - Language: {response.get('lang_code', 'N/A')}\n"
            f" - Administrator: {'Yes' if response.get('is_admin') else 'No'}\n\n"
            f"🏆 Rating and Awards\n"
            f" - Rating: {response.get('rating', 0)}\n"
            f" - Awards: {response.get('awards', 0)}\n\n"
            f"✨ Galaxy and Stars\n"
            f" - Galaxy: {response.get('galaxy', 0)}\n"
            f" - Stars: {response.get('stars', 0)} / {response.get('stars_max', 0)}\n"
            f" - Gifted Stars: {response.get('stars_gift', 0)}\n\n"
            f"🌌 Stardust\n"
            f" - Stardust: {response.get('dust', 0)} / {response.get('dust_max', 0)}\n"
            f" - Stardust Production: {response.get('dust_produce', 0)}\n"
            f" - Stardust Speed: {response.get('dust_speed', 0)}\n"
            f" - Stardust Progress: {response.get('dust_progress', 0) * 100:.2f}%\n\n"
            f"⏳ Time\n"
            f" - Created: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(response.get('created', 0)))}\n"
            f" - Stardust collection available from: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(response.get('dust_collect', 0)))}"
        )
