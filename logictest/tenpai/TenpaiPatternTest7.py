from maajanlib.logictest.tenpai import TenpaiPatternTest, TenpaiData7

class TenpaiPatternTest7(TenpaiPatternTest.TenpaiPatternTest):
	def test701六面待ち九連形1(self):
		self.executeTest(TenpaiData7.data701)

	def test702六面待ち九連形2(self):
		self.executeTest(TenpaiData7.data702)

	def test703六面待ち九連形3(self):
		self.executeTest(TenpaiData7.data703)

	def test704六面待ち５連続対子と暗刻(self):
		self.executeTest(TenpaiData7.data704)
