import re
import unidecode
import datetime as dt
from pathlib import Path

from pysubparser.utils import time_to_ms


TIMESTAMP_FORMAT = '%H:%M:%S,%f'


class Subtitle:
    """
    Class to data of a single subtitle.

    Attributes
    ----------
    index :
    text : str
        string containing every line of the subtitle without linebreaks
    duration : float
        time in milliseconds [ms] how long the subtitle is shown
    start : datetime object
        start time in HH:MM:SS,f to show subtitle (f: 3-digit [ms])
    end : datetime object
        stop time in HH:MM:SS,f to show subtitle (f: 3-digit [ms])
    text_lines : list[str]
        list of each line of the subtitle

    Methods
    -------
    add_text_line(text)
        Adds an entry to text_lines attribute of the Subtitle class.

    """

    def __init__(self, index, start=None, end=None, text_lines=None):
        """
        Parameters
        ----------
        index : int
            Inde of the subtitle
        start : datetime object
            start time in HH:MM:SS,f to show subtitle (f: 3-digit milliseconds)
        end : datetime object
            stop time in HH:MM:SS,f to show subtitle (f: 3-digit milliseconds)
        text_lines : list[str], optional
            list of each line of the subtitle. Could be empty during initiation
            and filled by add_text_line method

        """
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
        """Adds an entry to text_lines attribute of the Subtitle class.

        Parameters
        ----------
        text : str
            string representing a line of a subtitle
        """

        self.text_lines.append(text)

    def __repr__(self):
        return f"{self.start_string}-{self.end_string}\n{self.text} ({self.duration} ms.)\n"

