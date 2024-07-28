import logging

from common import configure_logging
from utils import do_something

logger = logging.getLogger(__name__)


def main():
    configure_logging(level=logging.DEBUG)
    logger.warning("Hello! Starting main")
    do_something()
    logger.warning("Bye! Finished main")


if __name__ == "__main__":
    main()
