import sys
def open_file(text):
    f_histogram = open("words.txt", "r")
    # lines = f_histogram.readlines()
    # lines = lines.strip()
    file_content = []
    for line in f_histogram:
        # split creates another list, if you use append, you will create a list of lists; but with extend you create just 1
        file_content.extend(line.split())
    return file_content

    #--------------------
def histogram(file_content):
    histogram = {}
    for word in file_content:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram
def unique_words(histogram):
    unique_words = 0
    for value in histogram.values():
        if value == 1:
            unique_words += 1
    return unique_words
def frequency(word, histogram):
    for key, value in histogram.items():
        if key == word:
            return value
if __name__ == "__main__":
    words = open_file("words.txt")
    print(histogram(words))
    unique_words(zmzdr)