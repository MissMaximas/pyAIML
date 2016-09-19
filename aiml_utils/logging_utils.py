__author__ = 'MissMaximas'

import logging
import sys


class LoggingUtils:

    LOGGING_LEVEL = logging.INFO

    log = logging.getLogger(__name__)

    def __init__(self):
        out_hdlr = logging.StreamHandler(sys.stdout)
        out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
        out_hdlr.setLevel(self.LOGGING_LEVEL)
        self.log.addHandler(out_hdlr)