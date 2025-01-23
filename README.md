
# 🌧 kaleidoscope
This is a (not) powerful Telegram userbot built using the Pyrogram framework. Automatization, Management, Fun.

## Requirements
Before you can run userbot, ensure that you have the following:

- Python 3.7+ installed
- API ID and API Hash


## Installation
Clone the repository:

```bash
git clone https://github.com/hkamori/kaleidoscope.git
cd kaleidoscope
```
Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```


## Commands

```
Ping:  (ping | pong | alive | check)
Info:  (info | kaleidoscope | userbot | about)
Help:  (help | commands)
Settings:  (settings | setvalue)
Stop:  (stop | exit)
Restart:  (restart | reboot)
SetPrefix:  (setprefix)
ExecLine:  (exec)
Translate:  (tr)
ILoveYou:  (ily)
Weather:  (weather)
```

# Implementing new modules
#### Step 1: Create a New Module File
1. Create a new ```.py``` file in the modules folder. For example, name it ```modulename.py```.

2. Add the necessary imports to your module file. For example, if you need a timer function, you would add:

```python
import time
```

3. Add commands list:

```python
commands = ['command', 'command2'] #add more if needed
```

4. Define the main function of your module:

```python
async def handle(app: Client, client: Client, message, args):
```

5. Write your code inside this function. For example, if you want to send a message using Pyrogram, use the following:

```python
await app.send_message(message.chat.id, "Your message here")
```

6. Working with Pyrogram: To create useful modules, it's important to know how to work with Pyrogram’s methods. Refer to the Pyrogram documentation if needed.

#### Step 2: Using Configuration Options
If your module requires reading or writing to a configuration file, import the configuration functions like this:

```python
from utils import config
```

You can then use the following functions:

- ```config.add_to_config(key, value)``` – Add or update a key-value pair.
- ```config.read_from_config(key)``` – Read a specific key from the config.
- ```config.read_all_keys()``` – Get all configuration keys.
- ```remove_from_config(key)``` – Remove key-value pair.

#### Final Notes
- Testing: Once you’ve added the command, test your module by running the bot and executing the command in a chat.
- Expanding: You can continue adding more functionality to your module as needed by using Pyrogram’s extensive methods and utilities.
By following these steps, you will be able to create and integrate custom modules into your userbot.

## Contributing

Feel free to fork the repository, submit issues, or contribute new features via pull requests.

- Fork the repository.
- Create a new branch ```(git checkout -b feature-branch)```.
- Make your changes.
- Commit the changes ```(git commit -m 'Add new feature')```.
- Push to the branch ```(git push origin feature-branch)```.
- Open a pull request.


## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)


