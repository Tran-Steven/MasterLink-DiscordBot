import discord
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.

bot = discord.Client(command_prefix='$',intents=discord.Intents.all())



@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("Master Link is in " + str(guild_count) + " town!")


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
  	await message.channel.send(get_domain_name(message))

def get_domain_name(url):
     try:
         results = get_sub_domain_name(url).split('.') # splits the URL so we can return only the last two elements (such as example.com)
         return results[-2] + '.' + results[-1] # returns only the last two elements in the list
     except:
         return 'gdn'

def get_sub_domain_name(url):
     try:
         return urlparse(url).netloc
     except:
         return 'subdomain' # ensures that at least something is returned


# EXECUTE BOT
bot.run(DISCORD_TOKEN)
