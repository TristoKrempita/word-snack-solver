import itertools
from nltk.corpus import words as nltk_words
def is_english_word(word,dictionary):
  # creation of this dictionary would be done outside of
  #     the function because you only need to do it once.

  try:
    x = dictionary[word]
    return True
  except KeyError:
    return False

def word_finder(letters):
  words = {}
  i=len(letters)
  dictionary = dict.fromkeys(nltk_words.words(), None)
  while i>1:
    for p in itertools.permutations(letters,i):
      #print((''.join(p)).lower(), " ",is_english_word((''.join(p)).lower())
      if is_english_word(''.join(p).lower(),dictionary) and ''.join(p) not in[ x for v in words.values() for x in v]:
        words.setdefault(str(i),[]).append(''.join(p))
    i-=1
  return words
