
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'Channel ID: {client._channel_id}')
    # now all pull messages from channel id

    _channel = client.get_channel(client._channel_id)



def main():
    bot_token = input("Enter the bot token: ")
    client._channel_id = int(input("Enter the channel ID: "))

    client.run(bot_token)
