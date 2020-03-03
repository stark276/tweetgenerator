import random
from histogram import open_file, histogram, frequency

histogram = (histogram(open_file('test.txt')))

# histogram = {"one": 1, "fish": 4, "two": 1, "blue": 1, "red": 1}


print(frequency("the", histogram(open_file())))
# print(frequency("of", histogram(open_file())))
# print(total_words(histogram(open_file())))
total_words = total_words(histogram)

print(total_words)

def stochastic(dic, total_words):
  rand_num = random.randint(1, total_words)
  # print(rand_num)
  total_value = 0
  for key,value in dic.items():
    # if rand_num <= value:
    # print("total_value", total_value)
    if rand_num - value - total_value <= 0:
      return key
    else:
      total_value += value