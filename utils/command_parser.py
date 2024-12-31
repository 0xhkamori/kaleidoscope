#------------------------------------------------------------
from typing import Tuple, Optional
from utils import config
#------------------------------------------------------------
def parse_command(text: str) -> Tuple[Optional[str], list]:
    """Parse command and arguments from message text.
    
    Args:
        text: The message text to parse
        
    Returns:
        A tuple containing:
        - The command (str) or None if no valid command
        - List of command arguments
    """
    prefix = config.read_from_config('prefix')
    if not text.startswith(prefix):
        return None, []
        
    parts = text[len(prefix):].strip().split()
    return (parts[0], parts[1:]) if parts else (None, [])
#------------------------------------------------------------
