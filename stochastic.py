import random

def histogram(file_content):
    histogram = {}
    for word in file_content:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def open_file():
    f_histogram = open("words.txt", "r")
    # lines = f_histogram.readlines()
    # lines = lines.strip()
    file_content = []
    for line in f_histogram:
        # split creates another list, if you use append, you will create a list of lists; but with extend you create just 1
        file_content.extend(line.split())
    return file_content

def sample(histogram):
    
    max = sum(histogram.values())
    randix = random.randint(1,max)
    


text = open_file()
hist = histogram(text)

results = {}

for i in range(10000):
    result = sample(hist)
    if result in results:
        results[result] += 1
    else:
        results[result] = 1

print(results)