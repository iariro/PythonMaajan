from maajanlib.logictest.tenpai import TenpaiPatternTest, TenpaiData1

class TenpaiPatternTest1(TenpaiPatternTest.TenpaiPatternTest):
	def test101嵌張(self):
		self.executeTest(TenpaiData1.data101)

	def test102辺張(self):
		self.executeTest(TenpaiData1.data102)

	def test103単騎待ち1(self):
		self.executeTest(TenpaiData1.data103)

	def test104単騎待ち2(self):
		self.executeTest(TenpaiData1.data104)

	def test105双石並の一面待ち(self):
		self.executeTest(TenpaiData1.data105)

	def test106両面の一面待ち(self):
		self.executeTest(TenpaiData1.data106)

	def test107ノベタンの変則形(self):
		self.executeTest(TenpaiData1.data107)
