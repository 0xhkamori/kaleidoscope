#-------------------------------------------------
import os
import importlib
import subprocess
from typing import Tuple, Optional, Dict, Any
from pathlib import Path
from pyrogram import Client
from pyrogram.types import Message
from utils import config
#-------------------------------------------------
class ModuleLoader:
    def __init__(self, modules_dir: str = "modules"):
        self.modules_dir = Path(modules_dir)
        self.modules: Dict[str, Any] = {}
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
#-------------------------------------------------
class CommandParser:
    def __init__(self):
        self.prefix = config.read_from_config('prefix')

    def parse(self, text: str) -> Tuple[Optional[str], list]:
        """Parse command and arguments from message text."""
        if not text.startswith(self.prefix):
            return None, []
        
        parts = text[len(self.prefix):].strip().split()
        return (parts[0], parts[1:]) if parts else (None, [])
#-------------------------------------------------
async def load_external_module(app: Client, message: Message) -> None:
    """Load an external module from a document."""
    try:
        downloads_dir = Path("downloads")
        downloads_dir.mkdir(exist_ok=True)
        
        file = await message.download()
        module_name = Path(message.document.file_name).stem
        
        importlib.import_module(f'downloads.{module_name}')
        
        subprocess.run(f'rm downloads/{message.document.file_name}', shell=True)
        target_path = Path("modules") / message.document.file_name
        await message.download(file_name=str(target_path))
        
        await app.send_message(
            message.chat.id,
            "✅  Module **loaded** successfully, restart your userbot.\n\n"
            "⚠  **Note:** If your module does not answer to messages, "
            "this means that your module is not implemented according to the instructions"
        )
    except Exception as error:
        await app.send_message(
            message.chat.id,
            f"📛  **Error loading module**: {str(error)}"
        )
#-------------------------------------------------
async def handle_message(client: Client, message: Message, app: Client) -> None:
    """Handle incoming messages and route them to appropriate handlers."""
    if message.document and message.caption:
        if message.caption.lower() in (".lm", ".loadmodule"):
            await load_external_module(app, message)
            return

    if not message.text:
        return

    parser = CommandParser()
    command, args = parser.parse(message.text)
    
    if not command:
        return

    await app.delete_messages(message.chat.id, message.id)

    module_loader = ModuleLoader()
    for module in module_loader.modules.values():
        if hasattr(module, 'commands') and command in module.commands:
            await module.handle(app, client, message, args)
            break
#-------------------------------------------------
