import re

#from pysubparser.classes.subtitle import Subtitle

FORMAT_TAG_CLEANER = re.compile(r'<[^>]*>', re.UNICODE)


def clean_format(subtitle):
    """
    Remove html format tags.

    subtitle: instance of subtitle class.
    """
    for i in range(len(subtitle.text_lines)):

        if FORMAT_TAG_CLEANER.search(subtitle.text_lines[i]):

            tag = FORMAT_TAG_CLEANER.search(subtitle.text_lines[i]).group(0)
            print(f"Remove tag: {tag}")

            subtitle.text_lines[i] = FORMAT_TAG_CLEANER.sub('', subtitle.text_lines[i])

    return subtitle
