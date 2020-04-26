from unidecode import unidecode

from pysubparser.classes.subtitle import Subtitle


def clean_ascii(subtitle):
    """
    Convert subtitle to ASCII.

    subtitle: instance of subtitle class.
    """
    for i in range(len(subtitle.text_lines)):

        subtitle.text_lines[i] = unidecode.unidecode(subtitle.text_lines[i])

    return subtitle
