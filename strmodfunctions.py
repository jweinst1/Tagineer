__author__ = 'Josh'

def join_with_spaces(lst):
	#joins together lists of strings into sentences
	index, counter, string = len(lst), 1, lst[0]
	while counter < index:
		string += ' '
		string += lst[counter]
		counter += 1
	return string
