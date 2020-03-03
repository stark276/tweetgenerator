from flask import Flask
from histogram import histogram



app = Flask(__name__)

@app.route('/')
def word_generator():
    my_file = open("./words.txt", "r")
    lines = my_file.readlines()
    my_histogram = histogram(lines)

    word = weighted_sample(my_histogram)
    return word

if __name__ == '__main__':
    app.run(debug=True)