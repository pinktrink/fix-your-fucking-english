from random import randint

from fyfe.models import Fix
from fyfe.views.utils import renderWordPage


def index(request):
	al = Fix.objects.all()
	fix = al[randint(0, len(al) - 1)]
	
	return renderWordPage(request, fix)
