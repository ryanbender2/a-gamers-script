import logging
from pathlib import Path
from typing import List
from runners.runner import Runner
from runners.epic_games import EpicGamesRunner
import os


class AGamersScript:
    def __init__(self, installers_output_dir: str) -> None:
        self.installers_output_dir = installers_output_dir
        downloads_dir = self.__constuct_download_dir_path__()
        self.runners: List[Runner] = [
            EpicGamesRunner(downloads_dir)
        ]

    def __constuct_download_dir_path__(self) -> Path:
        path = Path(self.installers_output_dir)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        return path

    def start(self) -> None:
        logging.info("Starting runners")
        for runner in self.runners:
            runner.start()
        for runner in self.runners:
            runner.join()
