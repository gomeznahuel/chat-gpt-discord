from app.discord_bot.discord_api import client, discord_token

def run():
    client.run(discord_token)

run()