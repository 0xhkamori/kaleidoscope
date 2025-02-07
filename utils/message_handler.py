# ░█░█░█░█░█▀█░█▄█░█▀█░█▀▄░▀█▀
# ░█▀█░█▀▄░█▀█░█░█░█░█░█▀▄░░█░
# ░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀             
# Name: utils/message_handler.py
# Description: Handle incoming messages and dispatch them to the appropriate modules.
# Author: hkamori | 0xhkamori.github.io
# ----------------------------------------------
# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ------------------------------------------------

from typing import Tuple, Optional, Dict, Any
from pathlib import Path
import importlib
import subprocess
from pyrogram import Client
from pyrogram.types import Message
from utils.config import config, add

class MessageHandler:
    def __init__(self, modules_dir: str = "modules"):
        self.modules_dir = Path(modules_dir)
        self.modules: Dict[str, Any] = {}
        self.prefix = config.get('prefix', '.')
        if not config.get('allowed_users'):
            add('allowed_users', [])
        self.load_modules()

    def load_modules(self) -> None:
        """Load all Python modules from the modules directory."""
        module_files = [
            f.stem for f in self.modules_dir.glob("*.py")
            if f.is_file() and f.stem != "__init__"
        ]
        self.modules = {
            name: importlib.import_module(f"modules.{name}")
            for name in module_files
        }

    def parse_command(self, text: str) -> Tuple[Optional[str], list]:
        """Parse command and arguments from message text."""
        if not text or not text.startswith(self.prefix):
            return None, []
        
        parts = text[len(self.prefix):].strip().split()
        return (parts[0], parts[1:]) if parts else (None, [])

    async def validate_user(self, message: Message, client: Client) -> bool:
        """
        Validate if the message sender is authorized to use commands.
        Returns True if user is the bot owner or in allowed_users list.
        """
        if not message.from_user:
            return False

        me = await client.get_me()
        
        if message.from_user.id == me.id:
            return True
            
        allowed_users = config.get('allowed_users', [])
        return message.from_user.id in allowed_users

    async def handle_message(self, client: Client, message: Message, app: Client) -> None:
        """Handle incoming messages with user validation."""
        if not await self.validate_user(message, client):
            return

        if not message.text:
            return

        command, args = self.parse_command(message.text)
        
        if not command:
            return

        await app.delete_messages(message.chat.id, message.id)

        for module in self.modules.values():
            if hasattr(module, 'commands') and command in module.commands:
                await module.handle(app, client, message, args)
                break

message_handler = MessageHandler()
