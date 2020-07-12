import re

#from pysubparser.classes.subtitle import Subtitle


BRACKETS_CLEANER = re.compile(r'''
        (\[|\()+      # opening bracket
        .*          # everything until
        (\]|\))+      # closing bracket
        '''
        , re.UNICODE|re.X)
        # closing bracket

def clean_brackets(subtitle):
    """
    Remove square OR round brackets and it's content.

    subtitle: instance of subtitle class.
    """

    for i in range(len(subtitle.text_lines)):

        if BRACKETS_CLEANER.search(subtitle.text_lines[i]):

            to_remove = BRACKETS_CLEANER.search(subtitle.text_lines[i]).group(0)

            print(f"Remove bracket & content: {to_remove}")
            subtitle.text_lines[i] = BRACKETS_CLEANER.sub('', subtitle.text_lines[i])

    return subtitle
