"""
Utils module for A Gamer's Script!

In here is utils used by the main file.
"""

from agamersscript import AGamersScript
from pathlib import Path
from multiprocessing import Process
from ui import AGamersScriptUI
import logging


def start_agamersscript() -> None:
    """start off the main class for downloading the installers."""
    gamer = AGamersScript()
    gamer.start()

def create_installers_directory() -> None:
    """Create the AGamersScript directory if it is not already created."""
    path = Path('./AGamersInstallers')
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def check_downloader(agamersscript_process: Process, ui: AGamersScriptUI) -> None:
    """Check if the agamersscript downloader process is still active. 
        Destory the ui when the process is finished. This is called every 500 ms
        by tkinter.

    Args:
        agamersscript_process (multiprocessing.Process): process running the agamersscript downloader.
        ui (AGamersScriptUI): the main AGamersScriptUI tkinter object.
    """
    if not agamersscript_process.is_alive():
        ui.quit()
    ui.after(250, check_downloader, agamersscript_process, ui)

def setup_logging() -> None:
    """Setup logging."""
    display_format = '[%(asctime)s %(name)s] %(levelname)s %(message)s'
    dt_fmt = '%m/%d/%Y %I:%M:%S %p'
    logging.basicConfig(format=display_format, level=logging.INFO, datefmt=dt_fmt)
