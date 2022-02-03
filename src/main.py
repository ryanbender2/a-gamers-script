from logger import setup_logging
import logging
from pathlib import Path
from agamersscript import AGamersScript


def create_installers_directory() -> None:
    """Create the AGamersScript directory if it is not already created."""
    path = Path('./AGamersInstallers')
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def main() -> None:
    setup_logging()
    create_installers_directory()
    logging.info("Starting AGamersScript")
    gamer = AGamersScript()
    gamer.start()

if __name__ == '__main__':
    main()
