from pyrogram import Client
from utils import config

commands = ["setvalue"]

async def handle(app: Client, client: Client, message, args):
    try:
        key = args[0]
        value = args[1]
        config.add(key, value)
        await app.send_message(message.chat.id, "✅  **Value set successfully**")
    except:
        await app.send_message(message.chat.id, "🛑  **The command is not used correctly**")
