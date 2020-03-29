from pathlib import Path
from datetime import datetime

# here needed ? spf: 29.03.2020 18:48
#from pysubparser.classes.classes import Subtitle, Subtitles
#from pysubparser.classes.exceptions import InvalidTimestampError




TIMESTAMP_SEPARATOR = ' --> '
TIMESTAMP_FORMAT = '%H:%M:%S,%f'


def write(subtitles, encoding=None, **kwargs):

    """
    Save subtitles to the source directory of the origin subtitles.

        subtitles: Instance of Subtitles Class.

    note: only srt implemented
    """
    # backup original version
    p = Path(subtitles.source)
    p.rename(p.with_suffix('.srt.orig'))

    index = 1

    if not encoding:
        # get encoding from Subtitles attribut
        encoding = subtitles.encoding

    with open(subtitles.source, mode='w', encoding=encoding) as file:

        for _,sub in subtitles.subs.items():
            file.write(f"{index}\n"\
                  f"{sub.start.strftime(TIMESTAMP_FORMAT)[:-3]}{TIMESTAMP_SEPARATOR}{sub.end.strftime(TIMESTAMP_FORMAT)[:-3]}\n")
            # TODO: list comprehension
            for line in sub.text_lines:
                file.write(f"{line}\n")
            # newline (separator) for subtitles
            file.write('\n')
            # count index
            index += 1




