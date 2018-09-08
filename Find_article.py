import wikipedia


def findarticle(article):
	
	#Finds the name of the closest article to user input
	search = wikipedia.search(article)
	article = search[0]
	
	#Stores the article as a string (for parsing and finding key words later)
	x = wikipedia.page(article)
	str_article = str(x.content)
	return str_article
	
