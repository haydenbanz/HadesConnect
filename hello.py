import discord
from discord.ext import commands

# Define your intents
intents = discord.Intents.default()
intents.typing = False  # You can adjust these based on your bot's needs
intents.presences = False

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
TOKEN = ''

# Create a bot instance with intents and a prefix for commands
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

# Command: !hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, World!')

# Start the bot
bot.run(TOKEN)
