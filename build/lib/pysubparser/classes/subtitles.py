import re
import unidecode
import datetime as dt
from pathlib import Path

from pysubparser.writer import write
from pysubparser.utils import time_to_ms, clean


class Subtitles:
    """
    Class to save all Subtitles of a movie.

    including it's type and
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

    def clean(self,
              to_lowercase=False,
              to_ascii=False,
              remove_brackets=True,
              remove_formatting=True,
              remove_formatted=False,
              remove_advertising=True,
              remove_names=True):

        "Clean subtitles."

        for _,subtitle in self.subtitles.items():

            subtitle = clean(subtitle,
                             to_lowercase=to_lowercase,
                             to_ascii=to_ascii,
                             remove_brackets=remove_brackets,
                             remove_formatting=remove_formatting,
                             remove_formatted=remove_formatted,
                             remove_advertising=remove_advertising,
                             remove_names=remove_names)

        #return subtitles

    def write(self, path=None, subtitle_type=None, encoding=None):
        """
        Save subtitles to disk (including a backup of original file).

        Default: origin directory, subtitle typ, and encodng.
        args:
            path:           path to file to save to
            subtitle_type:  (only srt implemented)
            encoding:       encoding as string, e.g. 'utf-8'
        """
        write(self, path = path, subtitle_type = subtitle_type, encoding = encoding)