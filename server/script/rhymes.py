import pdb
import sys


class Rhymes():
    root = None
    lookup = None

    class TrieNode():
        children = None
        values = None

        def __init__(self):
            self.children = {}
            self.values = []

        def add(self, value, key_sequence):
            if len(key_sequence) == 0:
                self.values.append(value)        # base case
            else:
                if key_sequence[0] not in self.children:
                    child = Rhymes.TrieNode()
                else:
                    child = self.children[key_sequence[0]]

                child.add(value, key_sequence[1:])
                self.children[key_sequence[0]] = child

        def traverse_sequence(self, key_sequence):
            if len(key_sequence) == 0:
                return self.values
            else:
                if key_sequence[0] in self.children:
                    child = self.children[key_sequence[0]]
                    return child.traverse_sequence(key_sequence[1:])
                else:
                    return []

        def all_children_values(self, key_sequence, depth_cutoff, level=0):
            if len(key_sequence) == 0:
                return self.values

            if level < depth_cutoff:
                return self.children[key_sequence[0]].all_children_values(key_sequence[1:], depth_cutoff, level+1)
            else:
                # will need to be optimized later
                acc = [] + self.values
                for child in self.children.values():
                    acc += child.all_children_values(
                        key_sequence[1:], depth_cutoff, level+1)
                return acc

    def __init__(self):
        #symbols = list(open('./script/cmudict-0.7b.symbols', 'rt'))

        symbols = list(open('./cmudict-0.7b.symbols', 'rt'))

        # print('# of symbols: %d' % len(symbols))

        self.lookup = {}
        self.root = self.TrieNode()
        # for line in open('./script/cmudict.0.7a', 'rt'):
        for line in open('./cmudict.0.7a', 'rt'):
            if line.startswith(';;;'):
                continue

            line = line.strip().split('  ')
            word, pronunciation = line[0], line[1].split(' ')

            # we want to search through the dictionary in reverse order
            # of the the pronunciation
            self.root.add(word, pronunciation[::-1])

            # create lookup table
            self.lookup[word] = pronunciation

    def pronunciation_of(self, word, capitalize=True):
        if capitalize:
            word = word.upper()
        return self.lookup[word] if word in self.lookup else None

    def ends_with(self, pronunciation, cutoff=2):
        return self.root.all_children_values(pronunciation[::-1], cutoff)


if __name__ == '__main__':
    rhymes = Rhymes()
    print('Pronunciation of "apple" is %s' %
          ' '.join(rhymes.pronunciation_of('apple')))
    print('Pronunciation of "gary" is %s' %
          ' '.join(rhymes.pronunciation_of('gary')))

    # while True:
    #word = raw_input()
    word = sys.argv[1]
    print(rhymes.pronunciation_of(word))
    print(rhymes.ends_with(rhymes.pronunciation_of(word), 2))
