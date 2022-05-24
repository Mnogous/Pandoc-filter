from sys import stderr
from panflute import *

headers = []

def sameheaders(elem, doc):
    if isinstance(elem, Header):
        head = stringify(elem)
        if head in headers:
            stderr.write(f"В тексте уже присутствует заголовок {head}\n")
        else:
            headers.append(head)

def uppheader(elem, doc):
    if isinstance(elem, Header):
        if elem.level <= 3:
            return Header(Str(stringify(elem).upper()), level=elem.level)

def bold(doc):
    doc.replace_keyword('BOLD', Strong(Str('BOLD')))

if __name__ == '__main__':
    run_filters([sameheaders, uppheader], prepare=bold)
