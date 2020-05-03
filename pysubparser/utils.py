from datetime import time

#from pysubparser.cleaners.advertising import clean_advertising
#from pysubparser.cleaners.lower_case import clean_lowercase
#from pysubparser.cleaners.formatting import clean_format
#from pysubparser.cleaners.brackets import clean_brackets
#from pysubparser.cleaners.whitespace import clean_whitespace


def time_to_ms(t: time) -> int:

    seconds = (t.hour * 60 + t.minute) * 60 + t.second
    return seconds  * 1000 + t.microsecond//1000

def clean(subtitle, to_lowercase=False, to_ascii=False, remove_brackets=True, remove_formatting=False, remove_advertising=True):

    "Clean single subtitle."

    if remove_advertising:

        # remove complete subtitle, if 1 line match advertising
        clean_advertising(sub)

    else:
        # clean every line of the subtitle
        if to_lowercase:
            sub = clean_lowercase(sub)
        if remove_brackets:
            sub = clean_brackets(sub)
        if remove_formatting:
            sub = clean_format
        if to_ascii:
            sub = clean_ascii(sub)
        sub = clean_whitespace(sub)


