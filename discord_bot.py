# bot.py
import os
import logging, discord, sys
from discord.ext import commands
from dotenv import load_dotenv
from alldebrid import AllDebrid

intents = discord.Intents.default()
intents.typing = True
intents.messages = True
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

bot = commands.Bot(command_prefix='!', intents=intents)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
dt_fmt = '%Y-%m-%d %H:%M:%S'
log_formatter = logging.Formatter('{asctime} {levelname}     {message}', dt_fmt, style='{')
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)
logger.info('Discord DebridBot is started')


@bot.command()
async def debrid(ctx, link):
    await ctx.send(f'Unlocking link...please wait')
    logger.info('A link has been asked to unlock')
    result = AllDebrid.unlockLink(link=link)
    if result['status'] == "success":
        formatted_result=discord.Embed(title="✅ Link Ready !", url=result['message'], description="Your link has been unlocked")
    else :
        formatted_result=discord.Embed(title="❗ Error !", description=result['message'])
    await ctx.send(embed=formatted_result)

bot.run(TOKEN)
