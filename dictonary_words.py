import random
import sys

file_content = []

with open("/usr/share/dict/words", "r") as f:

    for line in f:
        file_content.append(line.strip())
# print(file_content)

def random_sentence(words_list, length):
    choosen_words = []

    for _ in range(length):
        random_index = random.randint(0, len(words_list) - 1)
        choosen_words.append(words_list[random_index])
        # print(choosen_words)
        words_list.remove(words_list[random_index])

    print(" ".join(choosen_words))

if __name__ == "__main__":
    params = sys.argv[1:] 
    number = int(params[0])
    if number < 2:
        print("Not enough for sentence")
    elif number == None:
        print("not correct")
    else:
        random_sentence(file_content, number)