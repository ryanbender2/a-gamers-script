import logging
from typing import List
from runners.runner import Runner
from runners.epic_games import EpicGamesRunner
from runners.steam import SteamRunner
from runners.battlenet import BattleNetRunner
from runners.geforce_experience import GeForceExperienceRunner
from runners.discord import DiscordRunner
from runners.afterburner import MSIAfterburnerRunner
from runners.intel_xtu import IntelXTURunner
import tkinter as tk

class AGamersScript:
    """Main runner class for a gamers script.

        This class holds and starts off the list of runners that
        will go out and download the installers.
    """
    def __init__(self) -> None:
        self.runners: List[Runner] = [
            EpicGamesRunner(),
            SteamRunner(),
            BattleNetRunner(),
            GeForceExperienceRunner(),
            DiscordRunner(),
            MSIAfterburnerRunner(),
            IntelXTURunner()
        ]

    def start(self) -> None:
        logging.info("Starting runners")
        for runner in self.runners:
            runner.start()
        for runner in self.runners:
            runner.join()
