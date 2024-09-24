from googletrans import Translator
from pyrogram import Client

translator = Translator()

async def handle(app: Client, client: Client, message, args):
    phrase = " ".join(args)
    translation = translator.translate(phrase)
    await app.send_message(message.chat.id,
                            f"🧾 **Translated:** `{translation.text} ({translation.dest})`")
