import sys
from rhymes import Rhymes
import pdb
from related_words import related

word = sys.argv[1]

rhymes = Rhymes()
output = [x.lower()
          for x in rhymes.ends_with(rhymes.pronunciation_of(word), 2)]

print(related(word, output, 30))
