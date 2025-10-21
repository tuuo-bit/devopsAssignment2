class spellathon:
	def __init__( s, word_list_file, rest, centre):
		s.word_list = set( word_list_file.readlines())
		s.res = { 4: [], 5: [], 6: [], 7: []}
		s.rest, s.centre = rest, centre	
	def generate_words( s, file):
		letter = s.centre + s.rest
		for word_length in range( 4, 8):
			permutations = set( itertools.permutations( letters, word_length))
			for permutation in permutations:
				word_maybe = "".join( permutation)
				if s.centre in word_maybe and word_maybe+'\n' in word_list:
					s.res[word_length] += [word_maybe]
		return
	def give( s, word_length, num):
		return s.res[ min( num, len( s.res[word_length]))]