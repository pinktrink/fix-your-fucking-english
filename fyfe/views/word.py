from django.http import Http404

from fyfe.models import Search
from fyfe.views.utils import renderWordPage

def word(request, werd):
    try:
        search = Search.objects.get(word=werd)
        fix = search.fix
    except Search.DoesNotExist:
        raise Http404
    
    return renderWordPage(request, fix)
