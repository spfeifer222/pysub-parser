from pathlib import Path
from datetime import datetime

from pysubparser.utils import *
from pysubparser.classes.subtitle import Subtitle
from pysubparser.classes.subtitles import Subtitles
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

    subtitle_type = Path(path).suffix[1:]
    index = 0
    #subtitles = {}

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
                    yield subtitle
                    subtitle = None

    if clean:

       subtitle_clean = (sub.clean() for sub in subtitle)
       subtitles = Subtitles(subtitle_clean, path, subtitle_type=subtitle_type, encoding=encoding)

    else:

        subtitles = Subtitles(subtitle, path, subtitle_type=subtitle_type, encoding=encoding)

    return subtitles
