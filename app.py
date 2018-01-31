from flask import Flask
import insults
from random import choice

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def inbound():
	return generateInsult()

def generateInsult():
	word1 = choice(insults.word_one)
	word2 = choice(insults.word_two)
	word3 = choice(insults.word_three)
	return word1 + " " + word2 + " " + word3

if __name__ == "__main__":
	app.run(debug=True)


