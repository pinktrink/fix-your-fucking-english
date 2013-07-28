import re

from django.shortcuts import render

from fyfe.models import Search
from fyfe.views.utils import renderDescription


def fixit(request, werd, sentance):
	if werd.find(':') is not -1:
		described = []
		
		descriptions = []
		
		words = werd.split(':')
		
		incorrect = correct = sentance
		
		for word in words:
			correct = re.sub(r':(.*?):', '<em>' + word + '</em>', correct, 1)
			incorrect = re.sub(r':(.*?):', r'<em>\1</em>', incorrect, 1)
			
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
		
	else:
		correct = re.sub(r':(.*?):', '<em>' + werd + '</em>', sentance)
		incorrect = re.sub(r':(.*?):', r'<em>\1</em>', sentance)
		
		try:
			searchFix = Search.objects.get(word=werd).fix
			
			description = renderDescription(
				searchFix.description,
				[i.word for i in searchFix.search_set.all()]
			)
		
		except Search.DoesNotExist:
			description = ""
	
	return render(request, 'fyfe/fixit.html', {
		'correct' : correct,
		'incorrect' : incorrect,
		'description' : description
	})
