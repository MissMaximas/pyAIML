__author__ = 'chloe'

import logging
import sys


class LoggingUtils:

    log = logging.getLogger(__name__)

    def __init__(self):
        out_hdlr = logging.StreamHandler(sys.stdout)
        out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
        out_hdlr.setLevel(logging.INFO)
        self.log.addHandler(out_hdlr)
        self.log.setLevel(logging.INFO)
