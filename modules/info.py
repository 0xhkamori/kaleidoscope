import psutil
import platform
from pyrogram import Client
from utils import config

commands = ["info", "userbot", "about", "kaleidoscope"]

async def handle(app: Client, client: Client, message, args):
    me = config.read('mainemoji')
    ram_usage = psutil.virtual_memory().used / (1024 ** 3)
    total_ram = psutil.virtual_memory().total / (1024 ** 3)
    cpu_usage = psutil.cpu_percent()
    os_info = f"{platform.system()} {platform.release()}"

    await app.send_video(message.chat.id, "assets/info.mp4", caption=f"{me} `Kaleidoscope`\n🔹 Version: `0.5.0` #2\n\n🌠 **Ram usage**:  `{ram_usage:.0f}GB/{total_ram:.0f}GB`\n♻ **CPU Usage**:  `{cpu_usage}%`\n💻 **OS:**  `{os_info}`")
