import math

def get_cos_similarity_matrix(v1, v2):
  num = 0
  denom1 = 0
  denom2 = 0
  for i, v in enumerate(v1):
    num += v1[i] * v2[i]
    denom1 += v1[i] * v1[i]
    denom2 += v2[i] * v2[i]
  return (num / (math.sqrt(denom1) * math.sqrt(denom2)))