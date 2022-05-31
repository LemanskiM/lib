def hamming_distance(vec1, vec2):
  """
  compare 2 bin vector in distance 1 = +1
  vec1 - first binear
  vec2 - second binear compared
  """
  count = 0

  if len(vec1) != len(vec2):
    raise ValueError("Both vectors must be the same length.")

  for i in range (len(vec1)):
    if vec1[i] != vec2[i]:
      count+=1
  return count

def hamming_weight(vec1):
  """
  value of veight where 00000 is start vector and all 1 i transcript is +1 weight increase
  vec1 - compared vector to 000000
  """
  count = 0
  for i in range(len(vec1)):
    if int(vec1[i])==1:
      count+=1
    # u.count("1")
  return count
