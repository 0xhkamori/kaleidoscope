# #    __        __    _    __
# #   / /_____ _/ /__ (_)__/ /__  ___ _______  ___  ___
# #  /  '_/ _ `/ / -_) / _  / _ \(_-</ __/ _ \/ _ \/ -_)
# # /_/\_\\_,_/_/\__/_/\_,_/\___/___/\__/\___/ .__/\__/
# #                                         /_/

#-------------------------------------------------
import json
import os
import sys
import time
import threading
from pathlib import Path
from pyrogram import Client, filters
from utils.message_handler import handle_message
#-------------------------------------------------
class KaleidoscopeBot:
    def __init__(self):
        self.uptime = 0
        self.stop_toggle = False
        self.credentials = self._load_credentials()
        self.app = Client(
            "kaleidoscope",
            api_id=self.credentials['api_id'],
            api_hash=self.credentials['api_hash']
        )
        
    def _load_credentials(self) -> dict:
        """Load or create credentials file."""
        try:
            with open('credentials', 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return self._create_credentials()
            
    def _create_credentials(self) -> dict:
        """Prompt user for API credentials and save them."""
        print("Get your API ID and API Hash from my.telegram.org")
        credentials = {
            'api_id': input("Enter API ID: "),
            'api_hash': input("Enter API hash: ")
        }
        
        with open('credentials', 'w') as f:
            json.dump(credentials, f)
        return credentials

    def _uptime_counter(self):
        """Track bot uptime."""
        while not self.stop_toggle:
            time.sleep(1)
            self.uptime += 1

    @staticmethod
    def _display_banner():
        """Display the ASCII art banner."""
        os.system('cls' if os.name == 'nt' else 'clear')
        banner = """
        \033[95m __           .__         .__    .___                                       
        |  | _______  |  |   ____ |__| __| _/____  ______ ____  ____ ______   ____  
        |  |/ /\__  \ |  | _/ __ \|  |/ __ |/  _ \/  ___// ___\/  _ \\____ \_/ __ \ 
        |    <  / __ \|  |_\  ___/|  / /_/ (  <_> )___ \\  \__(  <_> )  |_> >  ___/ 
        |__|_ \(____  /____/\___  >__\____ |\____/____  >\___  >____/|   __/ \___  >
            \/     \/          \/        \/          \/     \/      |__|        \/ \033[92m
        """
        print(banner)

    def start(self):
        """Initialize and start the bot."""
        threading.Thread(target=self._uptime_counter, daemon=True).start()
        self._display_banner()
        print("\n\n                            🌧 Launch was successful!\033[94m")
        @self.app.on_message(filters.text & filters.me)
        async def message_handler(client, message):
            await handle_message(client, message, self.app)
        self.app.run()
#-------------------------------------------------
if __name__ == "__main__":
    bot = KaleidoscopeBot()
    bot.start()
#-------------------------------------------------
