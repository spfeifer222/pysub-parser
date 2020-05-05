import re
import unidecode
import datetime as dt
from pathlib import Path

from pysubparser.utils import time_to_ms


TIMESTAMP_FORMAT = '%H:%M:%S,%f'


class Subtitle:
    """
    Class to save times and content of a single subtitle.
    """

    def __init__(self, index, start=None, end=None, text_lines=None):
        self.index = index
        self.start = start
        self.end = end
        self.text_lines = text_lines if text_lines else []

    @property
    def text(self):
        return ' '.join(self.text_lines)

    @property
    def duration(self):
        return time_to_ms(self.end) - time_to_ms(self.start)

    @property
    def start_string(self):
        return self.start.strftime(TIMESTAMP_FORMAT)[:-3]

    @property
    def end_string(self):
        return self.end.strftime(TIMESTAMP_FORMAT)[:-3]

    def add_text_line(self, text):
        self.text_lines.append(text)

    def __repr__(self):
        return f"{self.start_string}-{self.end_string}\n{self.text} ({self.duration} ms.)\n"

