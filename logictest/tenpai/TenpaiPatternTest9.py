from logictest.tenpai import TenpaiPatternTest, TenpaiData9

class TenpaiPatternTest9(TenpaiPatternTest.TenpaiPatternTest):
	def test901九面待ち(self):
		self.executeTest(TenpaiData9.data901)
