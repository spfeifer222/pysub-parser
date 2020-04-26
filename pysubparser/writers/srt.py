from pathlib import Path
from datetime import datetime

# here needed ? spf: 29.03.2020 18:48
#from pysubparser.classes.classes import Subtitle, Subtitles
#from pysubparser.classes.exceptions import InvalidTimestampError

TIMESTAMP_SEPARATOR = ' --> '
TIMESTAMP_FORMAT = '%H:%M:%S,%f'


def write(subtitles, path, subtitles_type, encoding):

    """
    Save subtitles in srt format.

        subtitles: Instance of Subtitles Class.
        path: path to write subtitles file
        subtitle_type: srt (only implemented)
        encoding: encoding
    """
    # create pathlib object
    p = Path(path)

    if p == subtitles.source_path:
        # backup original version
        p.rename(p.with_suffix('.srt.orig'))

    index = 1


    with open(subtitles.source_path, mode='w', encoding=encoding) as file:

        print("Write subtiles to disk and skip empty subtitles...")

        # delete empty.subtitles since impossible in a loop
        to_delete = []
        [to_delete.append(_) for _,sub in subtitles.subtitles.items() if sub.text == '']

        # remove marked entries from.subtitles-dict
        for entry in to_delete:

            subtitles.subtitles.pop(entry)


        for _,sub in subtitles.subtitles.items():
            if sub.text == '':
                # remove empty subtitle
                #print(f"Skip empty subtitle on position {_}")
                # mark 'to_delete'
                to_delete.append(_)

            # TODO: don't write or better remove empty subtitle, DONE: 07.04.2020
            file.write(f"{index}\n"\
                  f"{sub.start.strftime(TIMESTAMP_FORMAT)[:-3]}{TIMESTAMP_SEPARATOR}{sub.end.strftime(TIMESTAMP_FORMAT)[:-3]}\n")
            # TODO: list comprehension
            for line in sub.text_lines:
                file.write(f"{line}\n")
            # newline (separator) for subtitles
            file.write('\n')
            # count index
            index += 1


        print("Done.")


