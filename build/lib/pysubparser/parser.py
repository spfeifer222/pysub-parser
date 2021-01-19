from pathlib import Path

from pysubparser.classes.exceptions import InvalidSubtitleTypeError
from pysubparser.parsers import srt, ssa, sub, txt

PARSERS = {
    'ass': ssa.parse,
    'ssa': ssa.parse,
    'srt': srt.parse,
    'sub': sub.parse,
    'txt': txt.parse
}

def parse(path, encoding = 'utf-8', **kwargs):

    subtitle_type = Path(path).suffix[1:]

    parser = PARSERS.get(subtitle_type.lower())

    if not parser:
        raise InvalidSubtitleTypeError(subtitle_type, PARSERS.keys())

    return parser(path, encoding, **kwargs)
