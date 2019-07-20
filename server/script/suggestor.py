import sys
from rhymes import Rhymes
import pdb


word = sys.argv[1]
rhymes = Rhymes()
output = ' '.join(rhymes.ends_with(rhymes.pronunciation_of(word), 2))
print(output)
