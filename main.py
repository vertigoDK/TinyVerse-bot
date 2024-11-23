from app.bot.bot import Bot
import asyncio
async def main():
    bot = Bot()
    await bot.run()
    
if __name__ == '__main__':
    asyncio.run(main()) 