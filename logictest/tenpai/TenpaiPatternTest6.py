from maajanlib.logictest.tenpai import TenpaiPatternTest, TenpaiData6

class TenpaiPatternTest6(TenpaiPatternTest.TenpaiPatternTest):
	def test601六面待ち九蓮宝燈暗刻除く(self):
		self.executeTest(TenpaiData6.data601)

	def test602六面待ち５連続対子1(self):
		self.executeTest(TenpaiData6.data602)

	def test603六面待ち５連続対子2(self):
		self.executeTest(TenpaiData6.data603)

	def test604六面待ち３面２筋(self):
		self.executeTest(TenpaiData6.data604)

	def test605六面待ち４枚使い1(self):
		self.executeTest(TenpaiData6.data605)
