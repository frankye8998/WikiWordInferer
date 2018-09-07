import wikipedia


def findarticle():
	article = input("Please enter a article name: ") # This line can be changed to take input from the webpage (or program?)
	
	#Finds the name of the closest article to user input
	search = wikipedia.search(article)
	article = search[0]
	
	#Stores the article as a string (for parsing and finding key words later)
	x = wikipedia.page(article)
	str_article = str(x.content)
	
