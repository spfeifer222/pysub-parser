import re

#from pysubparser.classes.subtitle import Subtitle

TAGGED = re.compile(r"""
    <[^>]*>     # openening tag
    .*          # content (text)
    </[^>]*>    # closing tag
""", re.UNICODE|re.X)


def clean_formatted(subtitle):
    """
    Remove html format tags AND its content.

    subtitle: instance of subtitle class.
    """
    for i in range(len(subtitle.text_lines)):

        if TAGGED.search(subtitle.text_lines[i]):

            tag = TAGGED.search(subtitle.text_lines[i]).group(0)
            print(f"Remove tag: {tag}")

            subtitle.text_lines[i] = TAGGED.sub('', subtitle.text_lines[i])

    return subtitle
