import re

#from pysubparser.classes.subtitle import Subtitle


BRACKETS_CLEANER = re.compile(r'\[[^[]*\]', re.UNICODE)


def clean_brackets(subtitle):
    """
    Remove square brackets and it's content.

    subtitle: instance of subtitle class.
    """

    for i in range(len(subtitle.text_lines)):

        if BRACKETS_CLEANER.search(subtitle.text_lines[i]):

            brackets = BRACKETS_CLEANER.search(subtitle.text_lines[i]).group(0)

            print(f"Remove bracket & content: {brackets}")
            subtitle.text_lines[i] = BRACKETS_CLEANER.sub('', subtitle.text_lines[i])

    return subtitle
