from pathlib import Path
from typing import Iterable

from pysubparser.classes.exceptions import InvalidSubtitleTypeError
#from pysubparser.classes.subtitles import Subtitles
from pysubparser.writers import srt

WRITERS = {
    'srt': srt.write
}

def write(subtitles, path = None, subtitle_type = None, encoding = None):
    """
    Write subtitles in subtitle_type format to file. If no path,
    subtitle_type, or encoding are given, the attributes
    subtiles.source_path, subtitles.subtitle_type, and subtitles.encoding
    of the subtitles class instance are taken and the original subtitles
    will be backuped.

        subtitles: Instance of Subtitles Class.
        path: path to write subtitles file
        subtitle_type: srt (only implemented)
        encoding: encoding
    """

    if not path:
        print(f"path = {path} ({type(path)}")
        print(f"subtitles = {subtitles} ({type(subtitles)}")
        path = subtitles.source_path

    if not subtitle_type:
        subtitle_type = Path(path).suffix[1:]

    if not encoding:
        # get encoding from Subtitles attribut
        encoding = subtitles.encoding


    writer = WRITERS.get(subtitle_type.lower())

    if not writer:
        raise InvalidSubtitleTypeError(subtitle_type, WRITERS.keys())

    return writer(subtitles, path, subtitle_type, encoding)
