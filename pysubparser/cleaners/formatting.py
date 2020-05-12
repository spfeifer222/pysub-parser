import re

#from pysubparser.classes.subtitle import Subtitle

FORMAT_OPEN_CLEANER = re.compile(r'<[^[]*>', re.UNICODE)
FORMAT_CLOSE_CLEANER = re.compile(r'</[^[]*>', re.UNICODE)


def clean_format(subtitle):
    """
    Remove html format tags.

    subtitle: instance of subtitle class.
    """
    for i in range(len(subtitle.text_lines)):

        subtitle.text_lines[i] = FORMAT_OPEN_CLEANER.sub('', subtitle.text_lines[i])
        subtitle.text_lines[i] = FORMAT_CLOSE_CLEANER.sub('', subtitle.text_lines[i])

    return subtitle
