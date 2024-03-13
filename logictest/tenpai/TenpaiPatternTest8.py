from logictest.tenpai import TenpaiPatternTest, TenpaiData8

class TenpaiPatternTest8(TenpaiPatternTest.TenpaiPatternTest):
	def test801八面待ち1(self):
		self.executeTest(TenpaiData8.data801)

	def test802八面待ち2(self):
		self.executeTest(TenpaiData8.data802)

	def test803八面待ち3(self):
		self.executeTest(TenpaiData8.data803)

	def test804八面待ち4(self):
		self.executeTest(TenpaiData8.data804)
