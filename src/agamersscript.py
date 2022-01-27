import logging
from typing import List
from runners.runner import Runner
from runners.epic_games import EpicGamesRunner
from runners.steam import SteamRunner
from runners.battlenet import BattleNetRunner


class AGamersScript:
    """Main runner class for a gamers script

        This class holds starts off the list of runners that
        will go out and download the installers.
    """
    def __init__(self) -> None:
        self.runners: List[Runner] = [
            # EpicGamesRunner(),
            # SteamRunner(),
            BattleNetRunner()
        ]

    def start(self) -> None:
        logging.info("Starting runners")
        for runner in self.runners:
            runner.start()
        for runner in self.runners:
            runner.join()
