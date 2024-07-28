import logging
from random import randint
from time import sleep

logger = logging.getLogger(__name__)


class User:

    def __str__(self):
        sleep(0.5)
        return f"{self.__class__.__name__}(id={id(self)})"


def something_expensive():
    sleep(0.5)
    return {"message": "something expensive"}


def do_something():
    number = randint(1, 100)
    fraction = 1.2345
    word = "123qwe'rty"
    user = User()
    logger.debug(
        "Prepare to do somthing, number: %s, word = %r, user: %s",
        number,
        word,
        user,
    )
    logger.info(
        "Doing something, number: %s, word = %r, %.2f user: %s",
        number,
        word,
        fraction,
        user,
    )
    if logger.isEnabledFor(logging.INFO):
        logger.info("Expensive info: %s", something_expensive())
    logger.warning("Done doing something")
