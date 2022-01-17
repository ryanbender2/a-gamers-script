import logging

def setup_logging() -> None:
    display_format = '[%(asctime)s %(name)s] %(levelname)s %(message)s'
    dt_fmt = '%m/%d/%Y %I:%M:%S %p'
    logging.basicConfig(format=display_format, level=logging.INFO, datefmt=dt_fmt)
