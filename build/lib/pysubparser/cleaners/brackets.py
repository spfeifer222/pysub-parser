import re

#from pysubparser.classes.subtitle import Subtitle


BRACKETS_FULL = re.compile(r'''
        (\[|\()+      # opening bracket
        .*            # everything until:
        (\]|\))+      # closing bracket
        '''
        , re.UNICODE|re.X)
BRACKETS_OPEN = re.compile(r'''
        (\[|\()+      # opening bracket
        .*            # everything until line end
        '''
        , re.UNICODE|re.X)
BRACKETS_CLOSE = re.compile(r'''
        .*            # everything until:
        (\]|\))+      # closing bracket
        '''
        , re.UNICODE|re.X)

def clean_brackets(subtitle):
    """
    Remove square OR round brackets and it's content.

    subtitle: instance of subtitle class.
    """

    for i in range(len(subtitle.text_lines)):

        if BRACKETS_FULL.search(subtitle.text_lines[i]):

            to_remove = BRACKETS_FULL.search(subtitle.text_lines[i]).group(0)
            print(f"Remove bracket & content: {to_remove}")
            subtitle.text_lines[i] = BRACKETS_FULL.sub('', subtitle.text_lines[i])

        if BRACKETS_OPEN.search(subtitle.text_lines[i]):

            to_remove = BRACKETS_OPEN.search(subtitle.text_lines[i]).group(0)
            print(f"Remove bracket & content: {to_remove}")
            subtitle.text_lines[i] = BRACKETS_OPEN.sub('', subtitle.text_lines[i])

        if BRACKETS_CLOSE.search(subtitle.text_lines[i]):

            to_remove = BRACKETS_CLOSE.search(subtitle.text_lines[i]).group(0)
            print(f"Remove bracket & content: {to_remove}")
            subtitle.text_lines[i] = BRACKETS_CLOSE.sub('', subtitle.text_lines[i])



    return subtitle
