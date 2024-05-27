
import discord
import json

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'Channel ID: {client._channel_id}')
    # now all pull messages from channel id

    _channel = client.get_channel(client._channel_id)

    data = []
    counter = 0

    async for message in _channel.history(limit=10**4):
        if message.content:
            message_data = {
                "author": message.author.name,
                "content": message.content,
                "timestamp": message.created_at.timestamp()
            }
            data.append(message_data)
        counter += 1
        if counter % 100 == 0:
            print(f"Processed {counter} messages")
        
        print("done!")

    with open(f"phase1/data{client._channel_id}.json", "w") as f:
        json.dump(data, f)


def main():
    #bot_token = input("Enter the bot token: ")
    #client._channel_id = int(input("Enter the channel ID: "))
    with open("phase1/secrets.json") as f:
        secrets = json.load(f)
        bot_token = secrets["token"]
        client._channel_id = int(secrets["channel"])

    client.run(bot_token)
