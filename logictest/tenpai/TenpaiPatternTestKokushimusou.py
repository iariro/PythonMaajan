from maajanlib.logictest.tenpai import TenpaiPatternTest, TenpaiDataKokushimusou

class TenpaiPatternTestKokushimusou(TenpaiPatternTest.TenpaiPatternTest):
	def test101(self):
		self.executeTest(TenpaiDataKokushimusou.data101)

	def test102(self):
		self.executeTest(TenpaiDataKokushimusou.data102)
