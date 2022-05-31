def compress(number):
  """
  compres the same numbers form left to right and put dots in place reapeted numbers

  XY_
  X - reapeted int
  Y - numbers of performers during
  _ - comma to next group of numbers

  """
  results = []
  for key, group in groupby(str(number)):
    results.append((key, "." * (len(list(group)))))
    # dodaj klucz i długość obiektu z itertools
  results = ["".join(item) for item in results]
    # pętla dla listy
  return "".join(results)

def decompress(codes):
  """
  decompress
  x = "34_52_76_78"
      YX_
  Y - number decopressed
  X - how many times decomressed

  """
  numbers = codes.split("_")
  result = ""
  for number in numbers:
    x =(number[0] *int(number[1]))
    result +=x
  return int(result)
