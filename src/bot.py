import argparse
import discord
import msg_handler


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--discord_token", required=True, type=str)
    args = ap.parse_args()
    start_bot(args.discord_token)


def start_bot(token):
    intents = discord.Intents.default()
    intents.message_content = True  # Requires 'MESSAGE CONTENT INTENT' turned on also
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop with its own message
        if message.author == client.user:
            return

        # Get event information
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # Send response
        await send_message(message, user_message)

    # Run bot with personal token
    client.run(token)


async def send_message(message, user_message):
    try:
        response = msg_handler.handle_user_msg(user_message)  # Handle message
        await message.channel.send(response)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
