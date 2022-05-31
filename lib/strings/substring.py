def get_slices(word, lenght):
    """
    return list of slices substrings
    word - input word
    lenght - lenght of substrings
    """


  NEW_WORDS = []
  if lenght < 1:
    raise ValueError("The lenght cant be less than 1")
  elif lenght > len(word):
    raise ValueError("Word cant be smallest than lenght")

  for i in range(0,len(word)-lenght+1):
    NEW_WORDS.append(word[i:i+lenght])
  return NEW_WORDS

get_slices("dasdwqw",2)
