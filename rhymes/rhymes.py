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
                child = Rhymes.TrieNode()
                child.add(value, key_sequence[1:])
                self.children[key_sequence[0]] = child

        def traverse_sequence(self, key_sequence):
            print(key_sequence)
            if key_sequence[0] not in self.children:
                return []
            else:
                child = self.children[key_sequence[0]]
                #ret = self.all_children_values(exclude=child) + \
                #        child.traverse_sequence(key_sequence[1:])
                ret = child.traverse_sequence(key_sequence[1:])
                return ret

        def all_children_values(self, exclude=None):
            all_values = [] + self.values
            for node in self.children.values():
                if node is exclude:
                    continue

                all_values.append(node.all_children_values())
            return all_values

    def __init__(self):
        symbols = list(open('cmudict-0.7b.symbols' , 'rt'))
        print('# of symbols: %d' % len(symbols))

        self.lookup = {}
        self.root = self.TrieNode()
        for line in open('cmudict.0.7a', 'rt'):
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

    def ends_with(self, pronunciation):
        return self.root.traverse_sequence(pronunciation[::-1])


if __name__ == '__main__':
    rhymes = Rhymes()
    print('Pronunciation of "apple" is %s' % ' '.join(rhymes.pronunciation_of('apple')))
    print('Pronunciation of "zsa" is %s' % ' '.join(rhymes.pronunciation_of('zsa')))
    print(rhymes.ends_with(rhymes.pronunciation_of('apple')))
