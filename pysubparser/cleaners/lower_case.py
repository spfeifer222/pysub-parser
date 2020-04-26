from pysubparser.classes.subtitle import Subtitle


def clean_lowercase(subtitle):
    """
    Make every character lower case.

    subtitle: instance of subtitle class.
    """
    for i in range(len(subtitle.text_lines)):
        subtitle.text_lines[i] = subtitle.text_lines[i].lower()

    return subtitle
