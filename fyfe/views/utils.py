import re

from django.shortcuts import render


def renderDescription(desc, words):
    desc = re.sub(r'-[\r\n]{1,2}', '<hr />', desc)
    desc = desc.replace('\n', '<br />')
    desc = re.sub(r'`(.*?)`', r'<em>\1</em>', desc)

    for word in words:
        r = re.compile(r'\b(' + word + r')\b', re.IGNORECASE)

        desc = re.sub(r, r'<em>\1</em>', desc)

    return desc

def renderWordPage(request, fix):
    words = [i.word for i in fix.search_set.all()]

    fix.description = renderDescription(fix.description, words)

    for word in words:
        r = re.compile(r'\b(' + word + r')\b', re.IGNORECASE)

        fix.title = re.sub(r, r'<em>\1</em>', fix.title)

    return render(request, 'fyfe/index.html', {
        'werd': fix
    })
