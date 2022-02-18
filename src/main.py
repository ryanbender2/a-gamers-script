from logger import setup_logging
import logging
from pathlib import Path
from agamersscript import AGamersScript
from multiprocessing import Process
from ui import AGamersScriptUI


def start_ui() -> None:
    """Start the GUI."""
    gui = AGamersScriptUI()
    gui.mainloop()

def create_installers_directory() -> None:
    """Create the AGamersScript directory if it is not already created."""
    path = Path('./AGamersInstallers')
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def main() -> None:
    setup_logging()
    create_installers_directory()
    logging.info("Starting AGamersScript")
    
    # start GUI in separate process
    gui_process = Process(target=start_ui)
    gui_process.start()

    # start AGamersScript and downloaders
    gamer = AGamersScript()
    gamer.start()

    # kill GUI when downloading is done
    gui_process.kill()

if __name__ == '__main__':
    main()
