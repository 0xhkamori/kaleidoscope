from pyrogram import Client
from utils import config

commands = ["setprefix"]

async def handle(app: Client, client: Client, message, args):
    me = config.read('mainemoji')
    new_prefix = " ".join(args)
    config.add_to_config('prefix', new_prefix)
    await app.send_message(message.chat.id, f"{me} **Prefix changed.** \n💫 New prefix: `({new_prefix})`")
