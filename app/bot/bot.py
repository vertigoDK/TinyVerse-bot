from .API import APIHandler
from ..telegram_bot.telegram_service import notify
import time
import config
from ..tools.generate_random_between_range import generate_random_between_range

class Bot:
    def __init__(self):
        # Time interval for collecting stars in seconds
        self.tolerance_from: int = config.TOLERANCE_FROM
        self.tolerance_to: int = config.TOLERANCE_TO
        self.api_handler = APIHandler()
        self.stats_per_request = config.STATS_PER_REQUEST


    async def run(self):
        if config.SEND_TO_TELEGRAM:
            await notify(message="Bot started!")
            
        stats_per_request = self.stats_per_request
            
        while True:

            try:
                
                # Collect stars through API
                response: dict[str, str] = self.api_handler.collect_stars()
                stats_per_request -= 1

                # Reset the statistics request counter
                # Notify about the collected dust
                if response["response"]["success"] == 1:
                    print(f"🌌 Successfully collected {response['response']['dust']} stardust.")


                if stats_per_request == 0:
                    response_stats: dict[str,str] = self.api_handler.check_stats()
                    
                    format_response_data = self._format_stats(response_stats)
                    
                    if config.SEND_TO_TELEGRAM:
                        await notify(
                            message=format_response_data
                        )
                    print(format_response_data)
                    stats_per_request = self.stats_per_request

                # try to buy stars     
                if config.STARS_AUTO_BUY:
                    self.api_handler.buy_stars()
                
                            
                # Random interval between requests
                time_to_collect: int = generate_random_between_range(self.tolerance_from, self.tolerance_to)
                
                time.sleep(time_to_collect)

            except Exception as e:
                time.sleep(time_to_collect)
                print(f"Error while processing {e}")
                await notify(message=f"Error while processing: {e}")









    def _format_stats(self, stats: dict) -> str:
        """
        Formats the statistics into a neat text for Telegram and the console.
        :param stats: Dictionary with statistics data.
        :return: Formatted string.
        """
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
