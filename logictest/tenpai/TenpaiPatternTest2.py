from maajanlib.logictest.tenpai import TenpaiPatternTest, TenpaiData2

class TenpaiPatternTest2(TenpaiPatternTest.TenpaiPatternTest):
	def test201両面(self):
		self.executeTest(TenpaiData2.data201)

	def test202双石並1(self):
		self.executeTest(TenpaiData2.data202)

	def test203ノベタン(self):
		self.executeTest(TenpaiData2.data203)

	def test204亜両面(self):
		self.executeTest(TenpaiData2.data204)

	def test205変則二面待ち(self):
		self.executeTest(TenpaiData2.data205)

	def test206変則二面待ち(self):
		self.executeTest(TenpaiData2.data206)

	def test207変則二面待ち(self):
		self.executeTest(TenpaiData2.data207)
