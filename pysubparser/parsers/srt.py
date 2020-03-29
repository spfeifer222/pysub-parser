from pathlib import Path
from datetime import datetime
from itertools import count

from pysubparser.classes.classes import Subtitle, Subtitles
from pysubparser.classes.exceptions import InvalidTimestampError

TIMESTAMP_SEPARATOR = ' --> '
TIMESTAMP_FORMAT = '%H:%M:%S,%f'


def parse_timestamps(line):
    try:
        start, end = line.split(TIMESTAMP_SEPARATOR)

        start = datetime.strptime(start, TIMESTAMP_FORMAT).time()
        end = datetime.strptime(end, TIMESTAMP_FORMAT).time()

        return start, end
    except:
        raise InvalidTimestampError(line, TIMESTAMP_FORMAT, 'srt')


def parse(path, encoding='utf-8', clean=True, **kwargs):

    subtype = Path(path).suffix[1:]
    index = 0
    subtitles = {}

    with open(path, encoding=encoding) as file:

        subtitle = None

        for line in file:
            line = line.rstrip()

            if not subtitle:
                if TIMESTAMP_SEPARATOR in line:

                    index += 1
                    start, end = parse_timestamps(line)
                    subtitle = Subtitle(index, start, end)
            else:
                if line:
                    subtitle.add_text_line(line)
                else:
                    if clean:
                        subtitle.clean_up()
                    # spf: return subtitle dict
                    subtitles[index] = subtitle
                    subtitle = None

    subtitles = Subtitles(subtitles, path, subtype=subtype)

    return subtitles


def write(subtitles, encoding='utf-8', **kwargs):

    """
    Save subtitles to the source directory of the origin subtitles.

        subtitles: Instance of Subtitles Class.

    note: only srt implemented
    """
    # backup original version
    p = Path(subtitles.source)
    p.rename(p.with_suffix('.srt.orig'))

    index = 1

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




