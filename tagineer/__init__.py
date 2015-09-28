__author__ = 'Josh'

import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [x for x in alphabet if x not in vowels]


def join_with_spaces(lst):
	#joins together lists of strings into sentences
	index, counter, string = len(lst), 1, lst[0]
	while counter < index:
		string += ' '
		string += lst[counter]
		counter += 1
	return string

class Word(str):

	def __init__(self, word):
		self.word = word
		self.tag = None
	def __getitem__(self, i):
		return self.word[i]
	def __len__(self):
		return len(self.word)
	def set_tag(self, part):
		self.tag = part

class Sentence(object):

	def __init__(self, text):
		self.words = [Word(elem) for elem in self.remove_punc(text)]
	def __repr__(self):
		return join_with_spaces(self.words)
	def __str__(self):
		return str(join_with_spaces(self.words))
	def __contains__(self, other):
		if other in [x.word for x in self.words]:
			return True
		else:
			return False
	def __len__(self):
		return len(self.words)
	def __getitem__(self, i):
		if i < 0:
			return False
		elif i > len(self.words)-1:
			return False
		else:
			return self.words[i]
	def index(self, elem):
		return self.words.index(elem)
	def get_previous(self, i):
		return self.words[i-1]
	def get_next(self, i):
		return self.words[i+1]
	def check_tag(self, i):
		if i < 0:
			return False
		elif i > len(self.words)-1:
			return False
		else:
			return self.words[i].tag
	def set_tag(self, i, tag):
		self.words[i].set_tag(tag)
	def append_tag(self, i, app):
		self.words[i].set_tag(self.words[i].tag+app)
	def show_tags(self):
		return [(elem, elem.tag) for elem in self.words]
	def is_last_word(self, i):
		if i == len(self.words)-1:
			return True
		else:
			return False
	def has_comma(self, i):
		if i < 0:
			return False
		elif i > len(self.words)-1:
			return False
		else:
			if self.words[i][len(self.words[i])-1] == ',':
				return True
			else:
				return False
	def remove_punc(self, text):
		if text[-1] == '?':
			self.question = True
			mod = list(text)
			mod.pop()
			mod = ''.join(mod)
			mod = mod.lower()
			return mod.split()
		else:
			self.question = False
			mod = list(text)
			mod.pop()
			mod = ''.join(mod)
			mod = mod.lower()
			return mod.split()
class Word_Ref (object):
	#used for part of speech tagging, and word look up.

	def __init__(self, selection):
		if selection == 'Verbs':
			wordfile = open('Verbs.txt', 'r')
			wordstring = wordfile.read()
			self.reference = wordstring.split()
			wordfile.close()
		elif selection == 'Nouns':
			wordfile = open('Nouns.txt', 'r')
			wordstring = wordfile.read()
			self.reference = wordstring.split()
			wordfile.close()
		elif selection == 'Adjectives':
			wordfile = open('Adjectives.txt', 'r')
			wordstring = wordfile.read()
			self.reference = wordstring.split()
			wordfile.close()
		elif selection == 'Adverbs':
			wordfile = open('Adverbs.txt', 'r')
			wordstring = wordfile.read()
			self.reference = wordstring.split()
			wordfile.close()
		elif selection == 'Pronouns':
			self.reference = ['i', 'me', 'my', 'mine', 'myself', 'you', 'your', 'yours', 'yourself', 'he', 'she', 'it', 'him', 'her'
							  'his', 'hers', 'its', 'himself', 'herself', 'itself', 'we', 'us', 'our', 'ours', 'ourselves',
							  'they', 'them', 'their', 'theirs', 'themselves', 'that', 'this']
		elif selection == 'Coord_Conjunc':
			self.reference = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']
		elif selection == 'Be_Verbs':
			self.reference = ['is', 'was', 'are', 'were', 'could', 'should', 'would', 'be', 'can', 'cant', 'cannot'
							  'does', 'do', 'did', 'am', 'been', 'go']
		elif selection == 'Subord_Conjunc':
			self.reference = ['as', 'after', 'although', 'if', 'how', 'till', 'unless', 'until', 'since', 'where', 'when'
							  'whenever', 'where', 'wherever', 'while', 'though', 'who', 'because', 'once', 'whereas'
							  'before', 'to', 'than']
		elif selection =='Prepositions':
			self.reference = ['on', 'at', 'in', 'of', 'into', 'from']
		else:
			raise ReferenceError('Must choose a valid reference library.')
	def __contains__(self, other):
		if other[-1] == ',':
			return other[:-1] in self.reference
		else:
			return other in self.reference
def tag_pronouns(statement):
	#will be first process, assumes no tag is given.
	pronouns = Word_Ref('Pronouns')
	i = 0
	while i < len(statement):
		if statement[i] in pronouns:
			statement.set_tag(i, 'pronoun')
			i += 1
		else:
			i += 1
	return statement

def tag_preposition(statement):
	preposition = Word_Ref('Prepositions')
	articles = ['the', 'an', 'a']
	i = 0
	while i < len(statement):
		if statement[i] in preposition:
			statement.set_tag(i, 'preposition')
			i += 1
		elif statement[i] in articles:
			statement.set_tag(i, 'article')
			i += 1
		else:
			i += 1
	return statement

def tag_be_verbs(statement):
	be_verbs = Word_Ref('Be_Verbs')
	i = 0
	while i < len(statement):
		if statement[i] in be_verbs:
			statement.set_tag(i, 'verb')
			i += 1
		else:
			i += 1
	return statement

def tag_subord_conj(statement):
	subord_conj = Word_Ref('Subord_Conjunc')
	i = 0
	while i < len(statement):
		if statement[i] in subord_conj:
			statement.set_tag(i, 'subord_conj')
			i += 1
		else:
			i += 1
	return statement

def tag_coord_conj(statement):
	coords = Word_Ref('Coord_Conjunc')
	i = 0
	while i < len(statement):
		if statement[i] in coords:
			statement.set_tag(i, 'coord_conj')
			i += 1
		else:
			i += 1
	return statement

def tag_avna(statement):
	adverbs = Word_Ref('Adverbs')
	verbs = Word_Ref('Verbs')
	nouns = Word_Ref('Nouns')
	adjectives = Word_Ref('Adjectives')
	i = 0
	while i < len(statement):
		if statement.check_tag(i) != None:
			i += 1
		else:
			if statement[i] in nouns:
				statement.set_tag(i, 'noun')
				i += 1
			elif statement[i] in verbs:
				statement.set_tag(i, 'verb')
				i += 1
			elif statement[i] in adverbs:
				statement.set_tag(i, 'adverb')
				i += 1
			elif statement[i] in adjectives:
				statement.set_tag(i, 'adjective')
				i += 1
			else:
				i += 1
	return statement

def post_processing(statement):
	#corrects errors in tagging based on rule-based deduction.
	be_verbs = ['is', 'was', 'are', 'were']
	i = 0
	while i < len(statement):
		if statement.check_tag(i) == 'noun' and statement.check_tag(i-1) == 'pronoun':
			statement.set_tag(i, 'verb')
			i += 1
		elif statement.check_tag(i) == None and statement.check_tag(i+1) == 'verb':
			statement.set_tag(i, 'noun')
			i += 1
		elif statement.check_tag(i) == None and statement.check_tag(i-1) == 'preposition':
			statement.set_tag(i, 'noun')
			i += 1
		elif statement.check_tag(i) == None and statement.check_tag(i+1) == 'subord_conj':
			statement.set_tag(i, 'noun')
			i += 1
		elif statement.check_tag(i) == 'noun' and statement.check_tag(i-1) == 'noun' and statement.has_comma(i-1) == False:
			statement.set_tag(i, 'verb')
			i += 1
		elif statement.check_tag(i) == 'noun' and statement.check_tag(i-1) == 'adjective' and statement.check_tag(i+1) == 'noun' and statement.is_last_word(i):
			statement.set_tag(i, 'adjective')
		elif statement.check_tag(i) == 'noun' and statement.check_tag(i-1) == 'article' and statement.check_tag(i+1) == 'noun':
			statement.set_tag(i, 'adjective')
			i += 1
		elif statement.check_tag(i) == 'noun' and statement[i-1] in be_verbs and statement.is_last_word(i) and statement.check_tag(i-2) == 'noun':
			statement.set_tag(i, 'adjective')
			i += 1
		elif statement.check_tag(i) == None and statement.check_tag(i-1) == 'article' and statement.check_tag(i+1) == 'noun':
			statement.set_tag(i, 'adjective')
			i += 1
		elif statement.check_tag(i) == 'noun' and statement.check_tag(i-1) == 'adverb':
			statement.set_tag(i, 'verb')
			i += 1
		else:
			i += 1
	return statement

def tag_noun_plurals(statement):
	i = 0
	while i < len(statement):
		if statement.check_tag(i) == 'noun':
			if statement[i][-1] == 's' and statement[i][-2] in consonants:
				statement.append_tag(i, '-P')
				i += 1
			elif statement[i][-1] == 's' and statement[i][-2] == 'e' and statement[i][-3] in consonants:
				statement.append_tag(i, '-P')
				i += 1
			else:
				statement.append_tag(i, '-S')
				i += 1
		else:
			i += 1
	return statement

def tag_sentence(statement):
	elem = statement
	tag = tag_avna(elem)
	tag = tag_pronouns(tag)
	tag = tag_preposition(tag)
	tag = tag_coord_conj(tag)
	tag = tag_subord_conj(tag)
	tag = tag_be_verbs(tag)
	tag = post_processing(tag)
	tag = tag_noun_plurals(tag)
	return tag

def tag_text(text):
	elem = Sentence(text)
	tag = tag_avna(elem)
	tag = tag_pronouns(tag)
	tag = tag_preposition(tag)
	tag = tag_coord_conj(tag)
	tag = tag_subord_conj(tag)
	tag = tag_be_verbs(tag)
	tag = post_processing(tag)
	tag = tag_noun_plurals(tag)
	return tag

def package_sentence(statement):
	#packages a tagged sentence into a displayable string
	counter = 0
	string = ""
	while counter < len(statement):
		if statement[counter].tag == None:
			string += statement[counter].word + " " + "\n"
			counter += 1
		else:
			string += statement[counter].word + " " + statement[counter].tag + "\n"
			counter += 1
	return string
#condition functions to check for nouns/subjects
#possible secondary processing arguments

def check_articles(i, statement):
	articles = ['the', 'a', 'an']
	if statement.get_previous(i) in articles:
		return True
	else:
		return False
def check_simpV(i, statement):
	simple = ['is', 'was', 'are', 'were', 'can', 'cannot', 'will', 'do', 'does', 'did' 'dont', 'would', 'could', 'should', 'has', 'had', 'have']
	if statement.get_next(i) in simple:
		return True
	else:
		return False

def precede_verb(i, statement):
	current = statement.get_next(i)
	if current[-1] == 's' and current[-2] in consonants:
		return True
	else:
		return False

