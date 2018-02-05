from textblob import TextBlob


class Engineering_Requirements():
	def __init__(self, text):
		self.text = text
		print('YES')

	def classes_for_software(self):
		problem_statement = TextBlob(self.text)
		print('YES')

		return problem_statement.noun_phrases


test = Engineering_Requirements("Engineer's should be able to plot the actual spending. The CIP Report should be loaded automatically. The PCS Report should be loaded automatically. The combination of spending and committed should be compiled into one dataframe.")
print(test.classes_for_software())