import re

from urlparse import unquote

from django.shortcuts import render

from fyfe.models import Search
from fyfe.views.utils import renderDescription


def fixit(request, werd, sentance):
    regex = re.compile(r':(.*?):')

    described = []

    descriptions = []

    words = filter(None, werd.split(':'))

    incorrect = correct = re.sub(r'(^|[^\+])(\+)($|[^\+])', r'\1 \3', sentance)

    for word in words:
        correct = unquote(re.sub(regex, '<em>' + word + '</em>', correct, 1))
        incorrect = unquote(re.sub(regex, r'<em>\1</em>', incorrect, 1))

        if word not in described:
            try:
                searchFix = Search.objects.get(word=word).fix

                allWords = [i.word for i in searchFix.search_set.all()]

                if not searchFix.supress_fixit_explanation:
                    descriptions.append(renderDescription(
                        searchFix.description,
                        allWords
                    ))

                described.extend(allWords)

            except Search.DoesNotExist:
                pass

                described.append(word)

    description = '<br /><hr /><br />'.join(descriptions)

    return render(request, 'fyfe/fixit.html', {
        'correct' : correct,
        'incorrect' : incorrect,
        'description' : description
    })
