def jaccard_similarity(textA, textB):
  textA = set(textA.split())
  textB = set(textB.split())
  intersection = set(textA).intersection(set(textB))
  union = set(textA).union(textB)
  similarity = len(intersection)/len(union)
  return similarity

jaccard_similarity(textA, textB)
