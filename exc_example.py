import logging

from common import configure_logging

log = logging.getLogger(__name__)


known_weather = {
    "sochi": {"rain_chance": 23},
}


def get_weather(city: str) -> dict | None:
    zero_div_err = None
    try:
        1 / 0
    except ZeroDivisionError as e:
        zero_div_err = e

    log.debug(
        "Zero division error: %r",
        zero_div_err,
        exc_info=zero_div_err,
    )
    try:
        return known_weather[city.lower()]
    except KeyError:
        # log.warning("Could not find city", exc_info=True)
        log.exception("Could not find city")
        return None


def main():
    configure_logging(level=logging.DEBUG)
    log.warning("Hello! Starting main")
    get_weather("Moscow")
    log.warning("Bye! Finished main")


if __name__ == "__main__":
    main()
