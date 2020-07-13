import re

from pysubparser.classes.subtitle import Subtitle


WHITESPACE_CLEANER = re.compile(r'\s+', re.UNICODE)
SPECIAL_SIGNS_NOTE = re.compile(r'â™ª')


def clean_whitespace(subtitle):
    """
    Change multiple whitespaces to single whitespace.

    subtitle: instance of subtitle class.
    """
    for i in range(len(subtitle.text_lines)):

        subtitle.text_lines[i] = WHITESPACE_CLEANER.sub(' ', subtitle.text_lines[i].strip())
        subtitle.text_lines[i] = SPECIAL_SIGNS_NOTE.sub('♪', subtitle.text_lines[i])

    return subtitle
