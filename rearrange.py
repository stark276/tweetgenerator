import random
import sys
def rearrange(sentence):
  words = sentence.split(" ")
  # print(split_words)
  new_sentence = []

  for _ in range(len(words)):
    random_index = random.randint(0, len(words) - 1) #one word index
    new_sentence.append(words[random_index])
    words.remove(words[random_index])
  
#   return (' '.join(new_sentence))
  print(' '.join(new_sentence))
  # print(new_sentence)

if __name__ == "__main__":
    sentence = " ".join(sys.argv[1:])
    rearrange(sentence)