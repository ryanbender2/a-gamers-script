from logger import setup_logging
import logging
from agamersscript import AGamersScript
import json

def main() -> None:
    setup_logging()
    logging.info("Starting AGamersScript")
    settings = json.load(open('config.json'))
    gamer = AGamersScript(settings['installers_output_directory'])
    gamer.start()

if __name__ == '__main__':
    main()
