import logging
from pathlib import Path
from time import sleep

from .runner import Runner

class EpicGamesRunner(Runner):
    def __init__(self, download_directory: Path) -> None:
        """Epic Games installer runner.

        Args:
            download_directory (Path): path to place the installer into.
        """
        super().__init__(headless=False)
        self.download_directory = download_directory
    
    def download_dependency(self) -> None:
        logging.info('Downloading Epic Games installer')
        self.browser.get('https://github.com/')
        sleep(2)
        