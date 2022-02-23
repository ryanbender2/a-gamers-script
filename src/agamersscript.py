import logging
from typing import List, Type
from multiprocessing import Process
from runners.runner import Runner
from runners.epic_games import EpicGamesRunner
from runners.steam import SteamRunner
from runners.battlenet import BattleNetRunner
from runners.geforce_experience import GeForceExperienceRunner
from runners.discord import DiscordRunner
from runners.afterburner import MSIAfterburnerRunner
from runners.intel_xtu import IntelXTURunner


def run_runner(runner_cls: Type[Runner]) -> None:
    """Run an installer script (Runner) thread.

    Args:
        runner_cls (Runner): runner clazz
    """
    runner = runner_cls()
    runner.start()

class AGamersScript:
    """Main runner class for a gamers script.

        This class holds and starts off the list of runners that
        will go out and download the installers.
    """
    def __init__(self) -> None:
        runner_clses: List[Runner] = [
            EpicGamesRunner,
            SteamRunner,
            BattleNetRunner,
            GeForceExperienceRunner,
            DiscordRunner,
            MSIAfterburnerRunner,
            IntelXTURunner
        ]

        """Processes to run the runners."""
        self.runners: List[Process] = [Process(target=run_runner, args=(runner_cls, )) for runner_cls in runner_clses]

    def start(self) -> None:
        logging.info("Starting runners")
        for runner in self.runners:
            runner.start()
        for runner in self.runners:
            runner.join()
