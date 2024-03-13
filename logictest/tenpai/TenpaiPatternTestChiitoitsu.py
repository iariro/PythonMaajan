from logictest.tenpai import TenpaiPatternTest, TenpaiDataChiitoitsu

class TenpaiPatternTestChiitoitsu(TenpaiPatternTest.TenpaiPatternTest):
	def test101(self):
		self.executeTest(TenpaiDataChiitoitsu.data101)

	def test102(self):
		self.executeTest(TenpaiDataChiitoitsu.data102)

	def test103(self):
		self.executeTest(TenpaiDataChiitoitsu.data103)
