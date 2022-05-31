def create_password():

    import random

    ints = range(33,127)
    paswwords= ''

    for i in range(16):
        paswwords+=chr(random.choice(ints))

    return("paswword it:" ,paswwords)

def throw_bones():

    import random

    x = input("how many times throw bones? ")
    x = int(x)
    dices = []
    mini = 1
    maxi = 6

    for i in range(x):
        dice = random.randint(mini,maxi)
        dices.append(dice)

    return(dices)

def lotto():
	import random

	myNumbers = []

	while len(myNumbers) < 6:
		newNumber = random.randint(1,49)
		if newNumber in myNumbers:
			print("Repeat :", newNumber)
			continue
		myNumbers.append(newNumber)
	print("Lotto 6 numbers:", myNumbers)

from collections import ChainMap

english_scoreboard = {
    ' ': 0,
    'EAIONRTLSU': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}
def scrabble_score(word):
    scores = ChainMap(*[dict.fromkeys(letter, score)
                        for letter, score in english_scoreboard.items()])
    return sum([scores[letter.upper()] for letter in word])

def clean_hashtags(input_file, output_file,lenght):
  """
  cleaning .txt file and saving clear data to new file
  """

  #read file
  with open(input_file, 'r') as file:
    hashtag = file.read()

  # splitting, pick correct lenght,append correct hash, del coppies, sort
  HASH_LIST = hashtag.split()
  l = []

  for hash in HASH_LIST:
    if len(hash)<=lenght+1:
      l.append(hash)
  l = list(dict.fromkeys(l))
  l.sort()

  #write hash in new line
  with open(output_file, "w") as file:
    for hash in l:
      file.write(hash + "\n")
