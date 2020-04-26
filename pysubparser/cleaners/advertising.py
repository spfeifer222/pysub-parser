import re


ADVERTING_CLEANER = re.compile(r'''

    .*?    # non-greedy match before adv
    (www\..*\.com|corrected[ ]*by|resync[ ]*by|subtitles) # adv keywords
    .*     # rest of the subtitle

    ''', re.UNICODE|re.VERBOSE|re.IGNORECASE|re.DOTALL)


def clean_advertising(subtitle):
    """
    Clean advertising. Remove complete subtitle, if 1 line match.

    subtitle: instance of subtitle class.
    """

    if ADVERTING_CLEANER.search(subtitle.text):

        subtitle.text_lines = []
