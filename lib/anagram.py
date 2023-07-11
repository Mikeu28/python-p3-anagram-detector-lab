
class Anagram:
    
    def __init__( self, given_word ):
        self.word = sorted( given_word )
        #print ( self.word )

    def match( self, word_match ):
        word_list = []
        for word in word_match:
            if ( sorted( word ) == self.word):
                word_list.append( word )
        return word_list

        

#a1 = Anagram("Hello")