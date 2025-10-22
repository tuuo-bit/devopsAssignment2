import itertools
class spellathon:
	def __init__( s, word_list_file, rest, centre):
		s.word_list = set( word_list_file.readlines())
		s.res = { 4: [], 5: [], 6: [], 7: []}
		s.rest, s.centre = rest.upper(), centre.upper()	
	def generate_words( s):
		letters = s.centre + s.rest
		for word_length in range( 4, 8):
			permutations = set( itertools.permutations( letters, word_length))
			for permutation in permutations:
				word_maybe = "".join( permutation)
				if s.centre in word_maybe and word_maybe+'\n' in s.word_list:
					s.res[word_length] += [word_maybe]
		return
	def give( s, word_length, num):
		return s.res[word_length][:min( num, len( s.res[word_length]))]

with open( 'word_list.txt', 'r') as file:
	while True:
		centre, rest = input( 'Enter space separated centre letter and the rest: ').split(' ')
		inst = spellathon( file, rest, centre)
		inst.generate_words()
		print( f"	~Generated Possible Solutions")
		l,n = map( int, input( 'Enter which length of words you want to see and how many, space separated: ').split(' '))
		print( f"	~Solution: { inst.give( l, n)}")