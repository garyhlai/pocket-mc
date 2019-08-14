

import gensim

gmodel = gensim.models.KeyedVectors.load_word2vec_format(
    "./GoogleNews-vectors-negative300.bin", binary=True, limit=20000)

target = "apple"
# potential rhymes
poten = ["royal", "awful", "oral", "anial"]
# a dict of words and their similarity
similarity = {}

for i in poten:
    try:
        similarity[i] = gmodel.similarity(i, target)
    # pass in case word not in the word2vec vocab
    except KeyError:
        pass

# only take the closest related rhymes
n = 2
result = sorted(similarity, key=similarity.get, reverse=True)
# if result is very long, we only take the n top items
if n < len(similarity):
    result = sorted(similarity, key=similarity.get, reverse=True)[:n]
print(result)
