from logger import setup_logging
import logging
from agamersscript import AGamersScript

def main() -> None:
    setup_logging()
    logging.info("Starting AGamersScript")
    gamer = AGamersScript()
    gamer.start()

if __name__ == '__main__':
    main()
