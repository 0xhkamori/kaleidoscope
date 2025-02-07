from pyrogram import Client
from utils import config

commands = ["stop", "exit"]

async def handle(app: Client, client: Client, message, args):
    global stop_toggle
    me = config.read('mainemoji')
    stop_toggle = True
    await app.send_message(message.chat.id, f"{me} `kaleidoscope` is now closed.`")
    exit()
