# ░█░█░█░█░█▀█░█▄█░█▀█░█▀▄░▀█▀
# ░█▀█░█▀▄░█▀█░█░█░█░█░█▀▄░░█░
# ░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀             
# Name: modules/help.py
# Description: Help module
# Author: hkamori | 0xhkamori.github.io
# ----------------------------------------------
# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ------------------------------------------------

import os
import importlib
from pyrogram import Client
from utils import config

commands = ["help", "commands"]

module_names = [
    name[:-3] for name in os.listdir("modules")
    if name.endswith(".py") and name != "__init__.py"
]
modules = {name: importlib.import_module(f"modules.{name}") for name in module_names}

commands_dict = {}
for module_name, module in modules.items():
    if hasattr(module, 'commands'):
        for command in module.commands:
            if module_name not in commands_dict:
                commands_dict[module_name] = []
            commands_dict[module_name].append(command)

async def handle(app: Client, client: Client, message, args):
    e = config.read('help_emoji')
    me = config.read('mainemoji')
    commands_count = sum(len(cmds) for cmds in commands_dict.values())
    modules_count = len(commands_dict)  # Count of unique modules
    msgtosend = f"{me} **{commands_count}** Commands available. **{modules_count}** modules.\n\n"

    for module_name, commands in commands_dict.items():
            commands_str = " | ".join(commands)
            msgtosend += f"{e} **{module_name.capitalize()}**:  ({commands_str})\n"
    await app.send_message(message.chat.id, msgtosend)
