rule1 = ['C', 'T', 'A', 'G']


def encodeDNA(character):
  charIndex = rule1.index(character)
  return '{0:02b}'.format(charIndex)


def decodeDNA(binary):
  charIndex = int(binary, 2)
  return rule1[charIndex]


# finish the following function
def XOR_DNA(plainDNA, keyDNA):

  # return the encoded DNA based on the key and rule
  return

  # EXTRA CREDIT


# MODIFY THE METHODS SO THAT USERS CAN CHOOSE FROM THE EIGHT POSSIBLE DNA RULES
# TRY TO FIGURE OUT THE RULES YOURSELF FIRST! IF YOU GET STUCK COME ASK ME :)
# REMEMBER WATSON CRICK SAYS A PAIRS WITH T & G PAIRS WITH C
