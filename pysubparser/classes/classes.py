import re
import unidecode
import datetime as dt
from pathlib import Path

from pysubparser.writers import srt
#from pysubparser.writters import sub.write      # not implemented
#from pysubparser.writters import txt.write      # not implemented
#from pysubparser.writters import ass.write      # not implemented
#from pysubparser.writters import ssa.write      # not implemented

WRITERS = {
    'srt': srt.write}
    #'sub': sub.write,                           # not implemented
    #'txt': txt.write,                           # not implemented
    #'ass': ssa.write,                           # not implemented
    #'ssa': ssa.write,                           # not implemented
#}

ALPHA_CLEANER = re.compile(r'[^\w\s\?]+', re.UNICODE)
BRACKETS_CLEANER = re.compile(r'\[[^[]*\]', re.UNICODE)
FORMAT_CLOSE_CLEANER = re.compile(r'</[^[]*>', re.UNICODE)
FORMAT_OPEN_CLEANER = re.compile(r'<[^[]*>', re.UNICODE)
WHITESPACE_CLEANER = re.compile(r'\s+', re.UNICODE)
ADVERTING_CLEANER = re.compile(r'''
                    .*?    # non-greedy match before adv
                    (www\.Addic7ed\.com|corrected by|subtitles) # adv keywords
                    .*     # rest of the subtitle
                    ''', re.UNICODE|re.VERBOSE|re.IGNORECASE|re.DOTALL)


def time_to_milliseconds(time):
    return ((time.hour * 60 + time.minute) * 60 + time.second) * 1000 + time.microsecond//1000


class Subtitles:
    """
    Class to save all Subtitles of a movie including it's type and
    original path.
    """

    def __init__(self, subtitles, source_path, subtype=None, encoding=None):
        self.subs = subtitles
        self.source = source_path
        self.encoding = encoding

    @property
    def subtype(self):
        return Path(self.source).suffix[1:]

    # old: def shift(self, time_in_ms):
    def shift(self, **kwargs):
        """
        Shift all subtitles using a datetime.timedelta object.

        **kwargs: accept all argument of a timedelta object:
                  days, seconds, microseconds, milliseconds, minutes,
                  hours, weeks
        """
        for _,sub in self.subs.items():
            # create timedelta object
            #old: delta = dt.timedelta(milliseconds=time_in_ms)
            delta = dt.timedelta(**kwargs)
            # create datetime objects & calculate
            date = dt.date(2000, 1, 1)
            start = dt.datetime.combine(date, sub.start) + delta
            end = dt.datetime.combine(date, sub.end) + delta
            # TODO; remove all entries, before date (before start time)
            # convert to time object and save
            sub.start = start.time()
            sub.end = end.time()

    def write(self, encoding=None, subtype=None, **kwargs):
        """
        Backup original subtitles and save actual subtitles to original
        destination and name.
        """

        if not subtype:
            # take original subtype
            subtype = self.subtype

        if not encoding:
            # take original encoding
            encoding = self.encoding

        writer = WRITERS.get(subtype.lower())

        if not writer:
            # TODO: create error class
            pass
            #raise InvalidSubtitleTypeError(subtype, PARSERS.keys())

        return writer(self, encoding=encoding, **kwargs)


class Subtitle:
    """**kwargs
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
    def clean(self):
        return self.clean_up(to_lowercase=False, to_ascii=False, remove_brackets=True, remove_formatting=False, remove_advertising=True)

    @property
    def duration(self):
        return time_to_milliseconds(self.end) - time_to_milliseconds(self.start)

    def add_text_line(self, text):
        self.text_lines.append(text)

    def clean_up(self, to_lowercase=False, to_ascii=False, remove_brackets=False, remove_formatting=False, remove_advertising=True):

        if remove_advertising:

            # remove complete subtitle, if 1 line match advertising
            if ADVERTING_CLEANER.search(self.text):

                self.text_lines = []

            else:

                for i in range(len(self.text_lines)):

                    if to_lowercase:
                        self.text_lines[i] = self.text_line[i].lower()

                    if remove_brackets:
                        self.text_lines[i] = BRACKETS_CLEANER.sub('', self.text_lines[i])

                    if remove_formatting:
                        self.text_lines[i] = FORMAT_CLOSE_CLEANER.sub('', self.text_lines[i])
                        self.text_lines[i] = FORMAT_OPEN_CLEANER.sub('', self.text_lines[i])

                    self.text_lines[i] = WHITESPACE_CLEANER.sub(' ', self.text_lines[i]).strip()

                    if to_ascii:
                        self.text_lines[i] = unidecode.unidecode(self.text_lines[i])

    def __repr__(self):
        return f'{self.start} | {self.text} ({self.duration} ms.)'

