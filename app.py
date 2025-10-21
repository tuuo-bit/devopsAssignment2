class spellathon:
	def __init__( s, word_list_file):
		s.word_list = word_list_file.readlines()
		s.res = { 4: None, 5: None, 6: None, 7: None}
	def take_input( s):
		s.rest, s.centre = map( str, input().split(' '))			
	def generate_words( s, file):
		return words	

#functions
def script():
      with open( "word_list.txt", "r") as file:
            store=[]
            letters=[ entry0.get(), entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get()]
            central_letter=letters[ 0].upper()
            other_letters="".join( letters[ 1:]).upper()
            subject=central_letter+other_letters
            if len( subject)+sum( map( lambda x: int( x.isalpha()), letters))==14:
                  word_list=set( file.readlines())
                  for word_length in range( 4, 8):
                              for permutation in set( itertools.permutations( subject , word_length)):
                                    word_maybe="".join( permutation)
                                    if central_letter in word_maybe and word_maybe+"\n" in word_list:
                                          store.append( word_maybe)
                  output.set( "\t".join( store))

def is_valid_entry( data):
      if ( data.isalpha() and len( data)==1) or data=="":
            return True
      else:
            return False