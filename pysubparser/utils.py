from datetime import time


def time_to_ms(t: time) -> int:
    seconds = (t.hour * 60 + t.minute) * 60 + t.second
    return seconds  * 1000 + t.microsecond//1000

def clean(subtitle, to_lowercase=False, to_ascii=False, remove_brackets=True, remove_formatting=False, remove_advertising=True):

    "Clean single subtitle."

    from pysubparser.cleaners.advertising import clean_advertising
    from pysubparser.cleaners.lower_case import clean_lowercase
    from pysubparser.cleaners.formatting import clean_format
    from pysubparser.cleaners.brackets import clean_brackets
    from pysubparser.cleaners.whitespace import clean_whitespace


    if remove_advertising:

        # remove complete subtitle, if 1 line match advertising
        clean_advertising(subtitle)

    else:
        # clean every line of the subtitle
        if to_lowercase:
            subtitle = clean_lowercase(subtitle)
        if remove_brackets:
            subtitle = clean_brackets(subtitle)
        if remove_formatting:
            subtitle = clean_format
        if to_ascii:
            subtitle = clean_ascii(subtitle)
        subtitle = clean_whitespace(subtitle)

