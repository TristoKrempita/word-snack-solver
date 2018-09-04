import itertools
import enchant
def word_finder(letters):
  words = {}
  d = enchant.Dict("en_US")
  i=len(letters)
  while i>1:
    for p in itertools.permutations(letters,i):
      if d.check(''.join(p)) and ''.join(p) not in[ x for v in words.values() for x in v]:
        words.setdefault(str(i),[]).append(''.join(p))
    i-=1
  return words
