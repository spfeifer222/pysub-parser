import re

#from pysubparser.classes.subtitle import Subtitle


NAMES_CLEANER = re.compile(r"""

        [A-Z]{2,}   # two or more CAPITAL letters
        :            # followed by a colon
        [ ]*         # if exists: whitespace(s)

        """, re.UNICODE|re.X)


def clean_names(subtitle):
    """
    Remove leading names in capital letters folowed by a colon
    and optional whitespace(s).

    subtitle: instance of subtitle class.
    """

    for i in range(len(subtitle.text_lines)):

        if NAMES_CLEANER.match(subtitle.text_lines[i]):
            name = NAMES_CLEANER.match(subtitle.text_lines[i]).group(0)
            print(f"Remove name: {name}")
            subtitle.text_lines[i] = NAMES_CLEANER.sub('', subtitle.text_lines[i])

    return subtitle
