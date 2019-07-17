from similarity.normalized_levenshtein import NormalizedLevenshtein
from similarity.jaccard import Jaccard


s1 = '中华人民共和国'
s2 = '中国'

normalized_levenshtein = NormalizedLevenshtein()
print('Levenshtein: ', normalized_levenshtein.distance(s1, s2))

jaccard_distance = Jaccard(1)
print('Jaccard: ', jaccard_distance.distance(s1, s2))

# print(jaccard_similarity_score(list(s1), list(s2)))




