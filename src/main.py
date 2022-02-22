from logger import setup_logging
import logging
from pathlib import Path
from agamersscript import AGamersScript
import multiprocessing
from ui import AGamersScriptUI


def start_agamersscript() -> None:
    """start off the main class for downloading the installers."""
    gamer = AGamersScript()
    gamer.start()

def create_installers_directory() -> None:
    """Create the AGamersScript directory if it is not already created."""
    path = Path('./AGamersInstallers')
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def main() -> None:
    setup_logging()
    create_installers_directory()
    logging.info("Starting AGamersScript")

    # start the agamersscript class in a separate process
    agamersscript_process = multiprocessing.Process(target=start_agamersscript)
    agamersscript_process.start()

    def check_downloader(agamersscript_process: multiprocessing.Process, ui: AGamersScriptUI) -> None:
        """Check if the agamersscript downloader process is still active. 
            Destory the ui when the process is finished. This is called every 500 ms
            by tkinter.

        Args:
            agamersscript_process (multiprocessing.Process): process running the agamersscript downloader.
            ui (AGamersScriptUI): the main AGamersScriptUI tkinter object.
        """
        if not agamersscript_process.is_alive():
            ui.quit()
        ui.after(500, check_downloader, agamersscript_process, ui)

    a_gamers_script_ui = AGamersScriptUI()
    a_gamers_script_ui.after(500, check_downloader, agamersscript_process, a_gamers_script_ui)
    a_gamers_script_ui.mainloop()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
