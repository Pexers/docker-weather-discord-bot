import os
import bot

# Get environment variables
TOKEN = os.getenv('BOT_TOKEN')

# Run bot
bot.run_discord_bot(TOKEN)
