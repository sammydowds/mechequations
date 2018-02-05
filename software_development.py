import nltk


class Engineering_Requirements():
	def __init__(self, text):
		self.text = text
		print('YES')

	def word_classification(self):
		text = nltk.tokenize.word_tokenize(self.text)

		print(nltk.pos_tag(text))

TEXT = "Everyone hates Chris. The software must process all requests for budgeting. The engineer must be able to choose the desired subtask."
test = Engineering_Requirements(TEXT)
test.word_classification()



