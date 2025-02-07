# ░█░█░█░█░█▀█░█▄█░█▀█░█▀▄░▀█▀
# ░█▀█░█▀▄░█▀█░█░█░█░█░█▀▄░░█░
# ░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀             
# Name: utils/config.py
# Description: Config system 
# Author: hkamori | 0xhkamori.github.io
# ----------------------------------------------
# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ------------------------------------------------

import os
import json
from typing import Any, Dict, Optional

class ConfigManager:
    """Manages configuration operations with file caching."""
    
    def __init__(self, config_file: str = 'config.json'):
        self.config_file = config_file
        self.default_config: Dict[str, Any] = {
            'prefix': '.',
            'help_emoji': '▫️',
            'trlang': 'en',
            'mainemoji': '🌧'
        }
        self._config_cache: Optional[Dict[str, Any]] = None
        self._initialize_config()

    def _initialize_config(self) -> None:
        """Initialize config file if it doesn't exist."""
        if not os.path.exists(self.config_file):
            self._save_config(self.default_config)
        self._load_config()

    def _load_config(self) -> None:
        """Load config from file into cache."""
        try:
            with open(self.config_file, 'r') as f:
                self._config_cache = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            self._config_cache = self.default_config
            self._save_config(self.default_config)

    def _save_config(self, config: Dict[str, Any]) -> None:
        """Save config to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
            self._config_cache = config
        except IOError as e:
            raise IOError(f"Failed to save config: {e}")

    def add_or_update(self, key: str, value: Any) -> None:
        """Add or update a config value."""
        if self._config_cache is None:
            self._load_config()
        self._config_cache[key] = value
        self._save_config(self._config_cache)

    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from config."""
        if self._config_cache is None:
            self._load_config()
        return self._config_cache.get(key, default)

    def get_all(self) -> Dict[str, Any]:
        """Get all config key-value pairs."""
        if self._config_cache is None:
            self._load_config()
        return self._config_cache.copy()

    def remove(self, key: str) -> bool:
        """Remove a key from config."""
        if self._config_cache is None:
            self._load_config()
        if key in self._config_cache:
            del self._config_cache[key]
            self._save_config(self._config_cache)
            return True
        return False

config = ConfigManager()

def add(key: str, value: Any) -> None:
    config.add_or_update(key, value)

def read(key: str) -> Any:
    return config.get(key)

def readAll() -> Dict[str, Any]:
    return config.get_all()

def remove(key: str) -> bool:
    return config.remove(key)
