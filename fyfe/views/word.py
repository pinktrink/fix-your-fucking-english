from fyfe.models import Search
from fyfe.views.utils import renderWordPage

def word(request, werd):
	search = Search.objects.get(word=werd)
	fix = search.fix
	
	return renderWordPage(request, fix)
