from find_article import findarticle
from vocabulary.vocabulary import Vocabulary as vb
from random import randint

list_of_words = findarticle("Barack")[1].split() # Imports the article and splits it into list of words


# Does some magic and stores typeofword as the type of word
key_words = {}


word_testing = randint(0,len(list_of_words))
while len(key_words) != 20:
	try:
		typeofword = vb.part_of_speech(list_of_words[word_testing], format="list")[0][0]
	except TypeError:
		typeofword = "False"
	if typeofword in ["preposition", "interjection", "conjunction", "False", "verb"]:
		word_testing = randint(0,len(list_of_words))
	else:
		key_words[word_testing] = (list_of_words[word_testing])
		word_testing = randint(0,len(list_of_words))
