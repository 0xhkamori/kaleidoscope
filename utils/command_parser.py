#------------------------------------------------------------
from utils import config
#------------------------------------------------------------
def parse_command(text):
    prefix = config.read_from_config('prefix')
    if text.startswith(prefix):
        command_parts = text.split(prefix)[1].strip().split()
        command = command_parts[0]
        args = command_parts[1:]
        return command, args
    return None, None
#------------------------------------------------------------
