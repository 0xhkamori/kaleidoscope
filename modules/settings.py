from pyrogram import Client
from utils import config

commands = ["settings", "config"]

async def handle(app: Client, client: Client, message, args):
    msg = "⚠  **Configuration**\n\n"
    p = config.read('prefix')
    cfgkeys = config.readAll()
    def transform_dict_to_list():
        """
        Transforms the dictionary of config into a list of [key, value] pairs.

        :return: A list of lists, where each inner list contains a key and its corresponding value
        """
        config_dict = config.readAll()
        return [[key, value] for key, value in config_dict.items()]
    config_list = transform_dict_to_list()

    for item in config_list:
        msg += f'❗ `{item[0]}` = "`{item[1]}`"\n'
    msg += f'\nℹ  To change or add new values, use `{p}setvalue (name) (value)`'
    await app.send_message(message.chat.id, msg)
