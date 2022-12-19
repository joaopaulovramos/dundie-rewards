import os
import logging
from logging import handlers


# BOILERPLATE
LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING').upper()
# TODO: Mover para modulo utilidades
log = logging.getLogger("dundie")

fmt = logging.Formatter(
      '%(asctime)s %(name)s %(levelname)s'
)


def get_logger(logfile='dundie.log'):
    """Returns a configured a logger"""

    # ch = logging.StreamHandler() #Console/terminal/stderr
    # ch.setLevel(LOG_LEVEL)
    fh = handlers.RotatingFileHandler(
      logfile,
      maxBytes=300,
      backupCount=10,
    )

    fh.setLevel(LOG_LEVEL)

    # ch.setFormatter(fmt)
    fh.setFormatter(fmt)

    # log.addHandler(fmt)
    log.addHandler(fmt)
