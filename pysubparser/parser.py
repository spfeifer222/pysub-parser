from pathlib import Path

from pysubparser.classes.exceptions import InvalidSubtitleTypeError

from pysubparser.parsers import srt
from pysubparser.parsers import ssa
from pysubparser.parsers import sub
from pysubparser.parsers import txt

PARSERS = {
    'ass': ssa.parse,
    'ssa': ssa.parse,
    'srt': srt.parse,
    'sub': sub.parse,
    'txt': txt.parse
}

WRITERS = {
    'srt': srt.write}
    #'sub': sub.write,
    #'txt': txt.write,
    #'ass': ssa.write,
    #'ssa': ssa.write,
#}

def parse(path, subtype=None, encoding='utf-8', **kwargs):

    if not subtype:
        subtype = Path(path).suffix[1:]

    parser = PARSERS.get(subtype.lower())

    if not parser:
        raise InvalidSubtitleTypeError(subtype, PARSERS.keys())

    return parser(path, encoding, **kwargs)


def write(subtitles, encoding='utf-8', subtype=None, **kwargs):
    "wirte subtitles to file."
    if not subtype:
        # take original subtype
        subtype = subtitles.subtype

    writer = WRITERS.get(subtype.lower())

    if not writer:
        # TODO: create error class
        pass
        #raise InvalidSubtitleTypeError(subtype, PARSERS.keys())

    return writer(subtitles, encoding, **kwargs)

