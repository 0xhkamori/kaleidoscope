# ░█░█░█░█░█▀█░█▄█░█▀█░█▀▄░▀█▀
# ░█▀█░█▀▄░█▀█░█░█░█░█░█▀▄░░█░
# ░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀             
# Name: modules/ily.py
# Description: ILY module
# Author: hkamori | 0xhkamori.github.io
# ----------------------------------------------
# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ------------------------------------------------

import asyncio
from asyncio.tasks import sleep
import requests
from pyrogram import Client

commands = ["ily"]

async def fetch_hearts_animation():
    response = await asyncio.get_event_loop().run_in_executor(
        None,
        lambda: requests.get("https://gist.githubusercontent.com/hikariatama/89d0246c72e5882e12af43be63f5bca5/raw/08a5df7255d5e925ab2ede1efc892d9dc93af8e1/ily_classic.json")
    )
    return response.json()

async def handle(app: Client, client: Client, message, args):
    hearts_animation = await fetch_hearts_animation()
    msg = await app.send_message(message.chat.id, '❤')
    await asyncio.sleep(0.5)
    for frame in hearts_animation:
        await app.edit_message_text(chat_id=msg.chat.id, message_id=msg.id, text=frame)
        await asyncio.sleep(0.5)
