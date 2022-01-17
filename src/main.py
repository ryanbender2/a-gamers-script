from logger import setup_logging
import logging


def main() -> None:
    setup_logging()
    logging.info("Starting")


if __name__ == '__main__':
    main()
