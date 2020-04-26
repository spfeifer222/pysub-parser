import re
import unidecode
import datetime as dt
from pathlib import Path

from pysubparser import writer
from pysubparser.utils import time_to_ms
from pysubparser.cleaners.advertising import clean_advertising
from pysubparser.cleaners.lower_case import clean_lowercase
from pysubparser.cleaners.formatting import clean_format
from pysubparser.cleaners.brackets import clean_brackets
from pysubparser.cleaners.whitespace import clean_whitespace


class Subtitles:
    """
    Class to save all Subtitles of a movie including it's type and
    original path.
    """

    def __init__(self, subtitles, source_path, subtitle_type=None, encoding=None):
        self.subtitles = subtitles
        self.source_path = source_path
        self.encoding = encoding

    @property
    def subtitle_type(self):
        return Path(self.source_path).suffix[1:]

    def shift(self, **kwargs):
        """
        Shift all subtitles using a datetime.timedelta object.

        kwargs: accept all argument of a timedelta object:
                days, seconds, microseconds, milliseconds, minutes,
                hours, weeks
        """
        for _,sub in self.subtitles.items():
            # create timedelta object
            delta = dt.timedelta(**kwargs)
            # create datetime objects & calculate
            date = dt.date(2000, 1, 1)
            start = dt.datetime.combine(date, sub.start) + delta
            end = dt.datetime.combine(date, sub.end) + delta
            # TODO; remove all entries, before variable date (before start time), Idea; put that in the writer, because there it's final
            # convert to time object and save
            sub.start = start.time()
            sub.end = end.time()

    def clean(self, to_lowercase=False, to_ascii=False, remove_brackets=True, remove_formatting=False, remove_advertising=True):

        "Clean subtitles."

        for _,sub in self.subtitles.items():

            if remove_advertising:

                # remove complete subtitle, if 1 line match advertising
                clean_advertising(sub)

            else:
                # clean every line of the subtitle
                if to_lowercase:
                    sub = clean_lowercase(sub)

                if remove_brackets:
                    sub = clean_brackets(sub)

                if remove_formatting:
                    sub = clean_format

                if to_ascii:
                    sub = clean_ascii(sub)

                sub = clean_whitespace(sub)
